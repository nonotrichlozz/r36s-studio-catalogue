# Anbernic RG Rotate — GammaOS Next 1.4.1

Fiche machine : [`consoles/anbernic-rg-rotate.json`](../consoles/anbernic-rg-rotate.json) (champ `procedures`).
Source officielle : <https://github.com/TheGammaSqueeze/GammaOSNext/releases/tag/v1.4.1-ANBERNICRGROTATE> (publiée le 13/08/2026).

| | |
|---|---|
| SoC | Unisoc T618 (« ums512 » dans les noms de fichiers), ARM64, 3 Go RAM, 32 Go eMMC |
| Écran | 3,5" 720×720 (1:1), coulissant/rotatif |
| Système installé | GammaOS Next 1.4.1 — Android 14, base LineageOS 21 |
| Où va le firmware | **Mémoire interne** (pas la carte SD) |
| Méthode | Mode *Download* Unisoc via USB + outil Windows `UpgradeDownload.exe` |
| Efface tout ? | Oui (installation complète). Non pour la restauration de la partition Super |

> ⚠️ **Différence majeure avec la R36S** : ici on ne flashe pas une carte SD. Le firmware s'écrit dans la mémoire interne par USB, et la carte SD doit même être **retirée** pendant l'opération. Dans R36S Studio, cette console relève donc du flux « je branche la console », pas « je mets la SD dans l'ordi ».

---

## 1. Ce qu'il faut avant de commencer

**Fichiers** (page de la release) :

| Variante | Fichiers | Résultat après extraction |
|---|---|---|
| **Lite** (recommandée) — sans services Google, meilleures perfs/autonomie | `ums512_1h10_rg_rotate_gammaos_1.4.1_lite.7z.001` + `.7z.002` | `ums512_1h10_rg_rotate_gammaos_1.4.1_lite.pac` |
| **Full** — avec services Google (Play Store, streaming) | `ums512_1h10_rg_rotate_gammaos_1.4.1_full.7z.001` + `.7z.002` | `ums512_1h10_rg_rotate_gammaos_1.4.1_full.pac` |
| Outils (toujours) | `UnisocTools_RG_ROTATE.zip` | dossiers `UnisocDrivers/` et `SPRD_Download_Tool/` |

**Logiciels sur le PC (Windows uniquement)** :
- 7-Zip (pour les archives fractionnées) ;
- Microsoft Visual C++ Redistributable **2005, 2008 et 2010**, en **x86 ET x64** ;
- pilotes USB UniSoc/Spreadtrum (fournis dans `UnisocTools`).

**Mot de passe de l'archive** : il n'est **pas** public. Il est réservé aux soutiens « GammaOS Insider » sur Patreon. R36S Studio ne doit ni le stocker ni le redistribuer : l'utilisateur le saisit lui-même.

---

## 2. Installation complète (efface la console)

### Étape 1 — Pilotes USB *(à faire une seule fois par PC)*
1. Extraire `UnisocTools_RG_ROTATE.zip`, ouvrir `UnisocTools/UnisocDrivers/`.
2. Lancer `DPInst64.exe` (droits admin). Sous Windows 11, le paquet Windows 10 fonctionne.
3. Contrôle : la console branchée en mode Download apparaît dans le Gestionnaire de périphériques avec un pilote UniSoc/SPRD.

### Étape 2 — Préparer le firmware
1. Mettre `.7z.001` et `.7z.002` dans le **même dossier**.
2. Clic droit sur `.7z.001` → *7-Zip → Extraire ici* → saisir le mot de passe.
3. On obtient **un seul** fichier `.pac` : c'est lui qu'on flashe.

### Étape 3 — Flasher
1. **Retirer toutes les cartes SD** de la console (sinon le SPL modifié peut tenter de démarrer dessus → écran noir).
2. Console **éteinte**, **aucun câble** branché.
3. Lancer `UnisocTools/SPRD_Download_Tool/UpgradeDownload.exe`.
4. *Charger le paquet* (icône dossier) → choisir le `.pac`. Vérifier que l'outil affiche bien la RG Rotate et la version 1.4.1.
5. Cliquer sur **Lecture / Démarrer** : l'outil se met en attente.
6. **Geste physique** : ouvrir la console en la faisant coulisser, **maintenir le bouton Retour** (au centre de la manette) **et brancher le câble USB** au PC.
7. Le flash démarre tout seul (barre de progression). **Ne rien débrancher.**
8. Statut « Réussi » / « OK » / « Reset » → la console redémarre et fait une réinitialisation d'usine. Débrancher le câble.

### Étape 4 — Premier démarrage
- Laisser le formatage se terminer, puis redémarrer.
- Le premier démarrage peut durer **2 à 3 minutes**, avec **jusqu'à 1 minute d'écran noir** : c'est normal.
- Suivre l'assistant Android → écran d'accueil GammaOS Next.

> Si le flash se bloque : maintenir **Retour + Volume Bas + Marche/Arrêt** ensemble jusqu'à ce qu'il redémarre.

---

## 3. Dépannage

| Symptôme | Solution |
|---|---|
| L'outil ne voit pas la console | Pilotes installés ? Console ouverte en coulissant, Retour **fermement** maintenu au branchement ? Changer de câble / de port USB. |
| Flash bloqué ou en erreur | Retour + Volume Bas + Marche/Arrêt jusqu'au redémarrage du flash. |
| Écran noir au démarrage | Le SPL tente de booter sur une SD invalide : retirer la SD, puis Volume Bas + Marche/Arrêt jusqu'au redémarrage. |
| Ne démarre pas sous GammaOS | Bon `.pac` RG Rotate ? Laisser le reformatage automatique se faire, sinon reflasher. Ensuite : issues GitHub GammaOS Next. |

---

## 4. Récupération après une OTA ratée (données conservées)

**Symptôme précis** : après une mise à jour OTA, écran noir et Marche/Arrêt + Volume Bas ne relance rien. La partition **Super** est corrompue ; on ne réécrit qu'elle.

1. Même `.pac` que pour l'installation (Lite ou Full) + `UnisocTools`.
2. Lancer `SPRD_Download_Tool/ResearchDownload.exe` (**pas** `UpgradeDownload.exe`). S'il manque : *SPD Research Tool R27.25.4601* (spdflashtool.com).
3. *Charger le paquet* → vérifier le titre (RG Rotate + version).
4. **Paramètres** (engrenage) → onglet principal → **décocher « Sélectionner tous les fichiers »** → cocher **uniquement Super** → OK.
5. Cliquer sur **Lecture** (flèche).
6. Brancher la console en maintenant **Volume Bas + Marche/Arrêt + Retour**.
7. Attendre : la console redémarre normalement. Sinon → installation complète (§2).

---

## 5. Revenir au firmware d'origine

Firmware Anbernic d'origine (Google Drive, lien dans la fiche JSON). Même manip que le §2 avec le `.pac` d'origine dans `UpgradeDownload.exe` : ouvrir la console, maintenir Retour, brancher l'USB. Sert aussi à débloquer une console.

---

## 6. Notes pour l'automatisation dans R36S Studio

Ce qui peut être automatisé, et ce qui restera un geste humain :

| Étape | Automatisable | Comment |
|---|---|---|
| Téléchargement des fichiers | ✅ | URLs de release stables (`releases/download/v1.4.1-ANBERNICRGROTATE/…`) |
| Visual C++ / 7-Zip | ⚠️ partiel | Installeurs silencieux, mais élévation admin |
| Pilotes UniSoc | ⚠️ partiel | `DPInst64.exe` (admin + avertissement Windows) ; détecter s'ils sont déjà là |
| Extraction | ✅ | `7z x …7z.001 -p<mdp>` (mot de passe saisi par l'utilisateur) |
| Retirer la SD, mode Download | ❌ | Geste physique : afficher une animation et **attendre la détection USB** |
| Détection de la console | ✅ | VID:PID Spreadtrum en mode Download, `1782:4d00` *(à confirmer sur la console)* |
| Flash | ⚠️ à étudier | Pistes ci-dessous |
| Post-flash (émulateurs) | ✅ | Enchaîner avec le module « Console Android » via ADB une fois GammaOS démarré |

**Pistes pour piloter le flash sans cliquer dans UpgradeDownload.exe** (aucune testée, à valider sur la RG Rotate) :
1. `CmdDloader.exe` — version ligne de commande de l'outil SPD, parfois incluse dans les paquets SPRD ; à chercher dans `SPRD_Download_Tool`.
2. Outils open source multiplateformes de flash Spreadtrum/Unisoc (famille `spd_dump` / `spreadtrum_flash`) : permettraient aussi le Mac et Linux, mais il faut extraire du `.pac` les FDL et images de partitions — risque de brique si mal fait.
3. En dernier recours : lancer `UpgradeDownload.exe` avec le `.pac` et guider l'utilisateur à l'écran.

**Licence / usage commercial** : le dépôt GammaOS Next est sous Apache-2.0, mais les builds sont derrière un mot de passe Patreon (`licence_a_verifier: true`). Avant de vendre le logiciel ou de livrer des consoles clients sous GammaOS, vérifier avec l'auteur (TheGammaSqueeze) ce qui est autorisé. Le logiciel ne doit jamais embarquer le `.pac` ni le mot de passe.

**Constaté lors de la première installation (27/10/2026, PC Windows 10 d'Arnaud)** :
- Le mot de passe n'est plus publié sur Patreon : depuis octobre 2026 il est distribué **uniquement sur le Discord GammaOS**, aux membres ayant le rôle Supporter (compte Patreon/Ko-fi relié à Discord).
- `UnisocTools_RG_ROTATE.zip` contient en réalité un dossier `UnisocTools_RG_VITA/` (mêmes outils) : `SPRD_Download_Tool/UpgradeDownload.exe` (R27.24.2301), **`CmdDloader.exe`** (flash en ligne de commande, piste n°1 pour l'automatisation), `UnisocDrivers/Win10/DPInst64.exe`, et `UnlockBootloader/` (contient `spd_dump.exe`). **`ResearchDownload.exe` est absent.**
- WinRAR extrait sans problème l'archive fractionnée chiffrée (7-Zip pas obligatoire).
- Le `.pac` Lite extrait fait **6,7 Go** ; UpgradeDownload l'affiche comme `RG_ROTATE_GAMMAOS_NEXT_LITE -- Version 1.4.1 -- 6365.291MB`, chargement ≈ 2 min.
- `DPInst64.exe` tourne en administrateur : l'automatisation par clics est bloquée par Windows (UIPI), l'utilisateur doit cliquer lui-même → dans R36S Studio, prévoir une installation silencieuse (`DPInst64.exe /S /SE /SW`) lancée avec élévation.
- Tailles des fichiers : lite .001 1,95 Go, .002 766 Mo ; full .001 1,95 Go, .002 871 Mo ; UnisocTools 55 Mo (SHA-256 publiés sur la page de release).

**Automatisation dans R36S Studio (branche `rg-rotate-gammaos`, 27/10/2026, jamais lancée sur la console)** :
- Flash par `CmdDloader.exe -pac <fichier.pac> -Version 2 -Port 0 -Timeout <ms> -Reset` (syntaxe lue dans le programme : `-Version 2` = mode UpgradeDownload, `-Port 0` = détection automatique). Repli : UpgradeDownload.exe avec le chemin du .pac copié.
- Extraction avec le 7-Zip fourni dans les outils (`SPRD_Download_Tool/System/Tools/7zip/32/7z.exe`), mot de passe transmis sans ligne de commande.
- Pilotes par `pnputil /add-driver …\Win10\Drivers\*.inf /install` (silencieux) plutôt que DPInst.
- Visual C++ : les outils n'utilisent que les bibliothèques 2010 et 2015+, déjà fournies dans `System/Dependency/` ; à confirmer sur un Windows vierge avant de retirer ce prérequis.
- Avant tout flash, l'en-tête du .pac est comparé à `pac_produit` (`ums512_1h10`), à la version et au `pac_nom` de la variante. `pac_produit` du firmware d'origine supposé identique (même carte), à confirmer.
- Restauration de la partition Super : pas automatisée (ResearchDownload.exe absent, sélection de partitions trop risquée sans essai).

**Statut de la fiche** : `non_verifie` — à passer à `verifie` une fois la manip réalisée sur la RG Rotate d'Arnaud (et le VID:PID confirmé).
