"""Valide le catalogue : chaque fiche de consoles/ contre schema/console.schema.json,
et index.json contre le contenu réel de consoles/.

Lancé par .github/workflows/validate.yml sur chaque pull request, et en local :

    pip install "jsonschema==4.26.0"
    python scripts/validate_catalogue.py

Code de sortie 1 dès qu'une erreur est trouvée (la pull request est bloquée).
Les avertissements ne bloquent pas.

Pourquoi ces règles, en plus du schéma : le Worker (r36s-studio-cloud) lit
index.json pour trouver une fiche, puis consoles/<id>.json. Une entrée d'index
sans fichier est une panne (404 côté Worker) ; un nom ou alias présent dans deux
entrées rend la recherche ambiguë (la première trouvée gagne -- SF3000 et
SF3000HD sont deux consoles distinctes).
"""

from __future__ import annotations

import json
import re
import sys
import unicodedata
from pathlib import Path

from jsonschema import Draft202012Validator, FormatChecker

ROOT = Path(__file__).resolve().parent.parent
SCHEMA_PATH = ROOT / "schema" / "console.schema.json"
INDEX_PATH = ROOT / "index.json"
CONSOLES_DIR = ROOT / "consoles"

# Même contrat que le Worker (catalogueClient.ts::CatalogueIndexEntry).
INDEX_SCHEMA = {
    "type": "object",
    "required": ["version", "consoles"],
    "additionalProperties": False,
    "properties": {
        "version": {"type": "string", "pattern": r"^\d+\.\d+\.\d+$"},
        "consoles": {
            "type": "array",
            "items": {
                "type": "object",
                "required": ["id", "nom", "alias", "statut"],
                "additionalProperties": False,
                "properties": {
                    "id": {"type": "string", "pattern": r"^[a-z0-9]+(-[a-z0-9]+)*$"},
                    "nom": {"type": "string", "minLength": 1},
                    "alias": {"type": "array", "items": {"type": "string", "minLength": 1}},
                    "statut": {"enum": ["verifie", "non_verifie"]},
                },
            },
        },
    },
}


def normalize_reference(text: str) -> str:
    """Identique à r36s-studio-cloud/worker/src/lib/normalize.ts."""
    text = unicodedata.normalize("NFD", text)
    text = "".join(c for c in text if not unicodedata.combining(c))
    return re.sub(r"\s+", " ", text.strip().lower())


def _load_json(path: Path, errors: list[str]):
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except UnicodeDecodeError as exc:
        errors.append(f"{path.relative_to(ROOT)} : pas de l'UTF-8 valide ({exc})")
    except json.JSONDecodeError as exc:
        errors.append(f"{path.relative_to(ROOT)} : JSON malformé, ligne {exc.lineno} colonne {exc.colno} ({exc.msg})")
    return None


def _schema_errors(validator: Draft202012Validator, data, label: str) -> list[str]:
    found = []
    for err in sorted(validator.iter_errors(data), key=lambda e: list(e.absolute_path)):
        where = "/".join(str(p) for p in err.absolute_path) or "(racine)"
        found.append(f"{label} : {where} -- {err.message}")
    return found


def validate() -> tuple[list[str], list[str]]:
    errors: list[str] = []
    warnings: list[str] = []

    schema = _load_json(SCHEMA_PATH, errors)
    if schema is None:
        return errors, warnings
    Draft202012Validator.check_schema(schema)
    validator = Draft202012Validator(schema, format_checker=FormatChecker())

    # --- fiches -----------------------------------------------------------
    sheets: dict[str, dict] = {}
    for path in sorted(CONSOLES_DIR.glob("*")):
        label = str(path.relative_to(ROOT))
        if path.is_dir() or path.suffix != ".json":
            errors.append(f"{label} : seuls des fichiers .json sont attendus dans consoles/")
            continue
        data = _load_json(path, errors)
        if data is None:
            continue
        found = _schema_errors(validator, data, label)
        errors.extend(found)
        if found or not isinstance(data, dict):
            continue
        if data["id"] != path.stem:
            errors.append(f"{label} : id « {data['id']} » différent du nom de fichier « {path.stem} »")
            continue
        sheets[data["id"]] = data

    # --- index.json ---------------------------------------------------------
    index = _load_json(INDEX_PATH, errors)
    if index is None:
        return errors, warnings
    index_validator = Draft202012Validator(INDEX_SCHEMA)
    found = _schema_errors(index_validator, index, "index.json")
    errors.extend(found)
    if found:
        return errors, warnings

    seen_ids: set[str] = set()
    names: dict[str, str] = {}
    for entry in index["consoles"]:
        cid = entry["id"]
        if cid in seen_ids:
            errors.append(f"index.json : id « {cid} » présent deux fois")
            continue
        seen_ids.add(cid)

        sheet_path = CONSOLES_DIR / f"{cid}.json"
        if not sheet_path.exists():
            errors.append(f"index.json : « {cid} » référencé mais consoles/{cid}.json n'existe pas (404 côté Worker)")
            continue
        sheet = sheets.get(cid)
        if sheet is None:
            continue  # fiche invalide, déjà signalée ci-dessus
        if entry["nom"] != sheet["identite"]["nom"]:
            errors.append(
                f"index.json : « {cid} » a le nom « {entry['nom']} » mais la fiche dit « {sheet['identite']['nom']} »"
            )
        if entry["statut"] != sheet["statut"]:
            errors.append(
                f"index.json : « {cid} » a le statut « {entry['statut']} » mais la fiche dit « {sheet['statut']} »"
            )
        if sorted(entry["alias"]) != sorted(sheet["identite"]["alias"]):
            errors.append(f"index.json : « {cid} » a des alias différents de ceux de la fiche")

        # Une même référence ne doit mener qu'à une seule fiche (findInIndex
        # renvoie la première correspondance, en silence).
        candidates = [cid, entry["nom"]] + (entry["alias"] if entry["statut"] == "verifie" else [])
        for candidate in candidates:
            key = normalize_reference(candidate)
            owner = names.get(key)
            if owner is not None and owner != cid:
                errors.append(f"index.json : « {candidate} » mène à la fois à « {owner} » et à « {cid} »")
            names.setdefault(key, cid)

    for cid in sorted(set(sheets) - seen_ids):
        warnings.append(
            f"consoles/{cid}.json n'est pas dans index.json : le Worker ne la servira jamais "
            f"tant qu'une entrée n'y est pas ajoutée (à faire en relisant la fiche)"
        )

    return errors, warnings


def main() -> int:
    errors, warnings = validate()
    for w in warnings:
        print(f"AVERTISSEMENT  {w}")
    for e in errors:
        print(f"ERREUR         {e}")
    sheets = len(list(CONSOLES_DIR.glob("*.json")))
    if errors:
        print(f"\n{len(errors)} erreur(s) sur {sheets} fiche(s) -- catalogue refusé.")
        return 1
    print(f"\n{sheets} fiche(s) valide(s), index.json cohérent ({len(warnings)} avertissement(s)).")
    return 0


if __name__ == "__main__":
    sys.exit(main())
