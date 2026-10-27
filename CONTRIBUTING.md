# Contribuer au catalogue

Ce catalogue est lu par R36S Studio pour dire à un utilisateur quoi installer
sur sa console — et surtout quoi **ne pas** installer. Une fiche fausse peut
faire flasher un système qui rend la carte inutilisable. Chaque contribution
doit donc permettre de distinguer ce qui a été **vérifié** de ce qui est
**supposé**.

## Toute pull request doit indiquer

1. **Le modèle exact de la console** — nom commercial *et* ce qui permet de le
   distinguer des modèles voisins (révision, écran, puce, inscription au dos,
   photo). Exemples de pièges réels : SF3000 et SF3000HD ; R36S d'origine et
   ses clones.
2. **Ce qui a été testé sur la console elle-même** — quelle version de quel
   firmware, quelle manipulation, quel résultat observé à l'écran. « Démarre et
   lance un jeu » n'est pas la même chose que « la documentation dit que ça
   marche ».
3. **La distinction vérifié / supposé, champ par champ** :
   - vérifié sur matériel → le dire, avec la date ;
   - lu dans une documentation, un dépôt ou un forum → donner le lien dans
     `sources` ou `source_url`, et ne pas le présenter comme testé ;
   - dans `symptomes[]`, `verifie_sur_materiel: true` seulement si le symptôme
     **et** sa cause ont été constatés sur une vraie console, la cause
     confirmée en premier.

Une PR qui ne précise pas ces trois points reste ouverte avec une demande de
précision ; elle n'est pas fusionnée.

## Règles de fond

- **Une fiche par modèle.** Si deux consoles se ressemblent mais diffèrent
  (puce, écran, firmware), ce sont deux fiches. Aucun `alias` générique
  (« Game Console », « Handheld ») : un alias mène à une seule fiche.
- **`incompatibles` n'accueille que du confirmé** (flash qui échoue, carte
  inutilisable, architecture incompatible), jamais du « non testé ».
- **Licences** : recopier la licence du projet lui-même, pas celle d'un
  composant qu'il embarque. Mention non commerciale → `restriction_commerciale:
  true`.
- **Aucune ROM, aucun BIOS, aucune image système**, ni en pièce jointe ni en
  lien de téléchargement.
- **`index.json`** : une fiche n'est servie par R36S Studio qu'une fois ajoutée
  à l'index. L'ajout se fait à la relecture, par la personne qui fusionne —
  `statut: "verifie"` seulement si quelqu'un a pu la contrôler sur matériel.

## Fiches générées automatiquement

Les PR « Fiche non vérifiée : … » sont ouvertes par la recherche IA de R36S
Studio (`statut: "non_verifie"`). Elles sont des **points de départ** : même
exigence que ci-dessus avant toute fusion, sources relues une par une.

## Validation automatique

Chaque PR est vérifiée par `.github/workflows/validate.yml` : chaque fiche de
`consoles/` contre `schema/console.schema.json`, et la cohérence de
`index.json` (fichier présent, même nom et même statut, aucun alias partagé
entre deux fiches). Pour la lancer avant d'ouvrir la PR :

```
pip install "jsonschema==4.26.0"
python scripts/validate_catalogue.py
```
