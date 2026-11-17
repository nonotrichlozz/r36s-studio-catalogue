# R36S — portages natifs et recompilations (PortMaster)

Console : **R36S** (puce RK3326, ArkOS / dArkOS). Aucun jeu n'est fourni : chaque
portage demande les fichiers d'un jeu que l'on possède.

> **Statut : non vérifié, sauf mention contraire.** Liste établie le 2026-11-17
> à partir d'une réponse de Gemini, puis recoupée avec les pages GitHub (les dépôts
> existent ; ce que chaque README annonce est noté ci-dessous). Seul **Halo** a été
> constaté fonctionnel sur une vraie R36S (par Aretro, 2026-11-17).

| # | Jeu | Technique | Fichiers à fournir | Statut |
|---|-----|-----------|--------------------|--------|
| 1 | [Halo: Combat Evolved](#1-halo-combat-evolved) | Décompilation ARM64 | ISO Xbox | **Confirmé sur R36S** |
| 2 | [Need for Speed: Underground 2](#2-need-for-speed-underground-2) | Recompilation statique | Version PC (v1.0 ou v1.2) | README cite la R36S |
| 3 | [Need for Speed: Most Wanted](#3-need-for-speed-most-wanted-2005) | Wrapper Android | APK + OBB | README cite la R36S (alpha) |
| 4 | [Need for Speed II SE](#4-need-for-speed-ii-se) | Réimplémentation open source | Version PC Special Edition | Officiel PortMaster (à vérifier) |
| 5 | [Need for Speed: Porsche Unleashed](#5-need-for-speed-porsche-unleashed) | Moteur Open-Unleashed | Version PC | R36S non confirmée |
| 6 | [Resident Evil 4](#6-resident-evil-4-mobile--platinum) | Wrapper mobile/iOS | IPA ou APK/OBB | README cite la R36S (bêta) |
| 7 | [Zelda: The Wind Waker](#7-zelda-the-wind-waker) | Recompilation GameCube | ISO GameCube (US) | Non lu (Discord) |
| 8 | [GTA: Vice City](#8-gta-vice-city) | Portage PC (officiel PortMaster) | Fichiers du jeu PC | **Confirmé sur R36S** |

---

## 1. Halo: Combat Evolved

- **Technique :** décompilation native ARM64, sans émulation.
- **Fichiers requis :** une image ISO Xbox originale du jeu.
- **Portage :** https://github.com/kirklandsig/halo-ce-anbernic-rg35xx — à récupérer via l'archive zip PortMaster.
- **Statut :** **fonctionne sur R36S** (constaté par Aretro). Attention : le README du dépôt vise les Anbernic à puce H700 sous Knulli et ne cite pas la R36S ; noter ici le build/zip exact utilisé sur la R36S.
- **Capture :** à ajouter (idéalement une photo de ta propre R36S).

## 2. Need for Speed: Underground 2

- **Technique :** recompilation statique de l'exécutable PC vers ARM64.
- **Fichiers requis :** données complètes de la version PC (v1.0 ou v1.2).
- **Portage :** https://github.com/manuelpllull/nfsu2-recompiled-r36s (README : « R36S & PortMaster ARM64 Port »).
- **Capture :** à ajouter.

## 3. Need for Speed: Most Wanted (2005)

- **Technique :** couche de compatibilité (wrapper) qui exécute le moteur de l'édition mobile Android.
- **Fichiers requis :** APK et OBB de l'édition mobile Android.
- **Portage :** https://github.com/EapRules/nfsmw-r36s (README : alpha publique pour R36S, installation via PortMaster).
- **Capture :** à ajouter.

## 4. Need for Speed II SE

- **Technique :** réimplémentation open source du moteur d'origine, présentée comme validée dans PortMaster.
- **Fichiers requis :** dossiers de données de la version PC Special Edition.
- **Portage :** fiche « Wiki de Need For Speed II SE - PortMaster » : https://share.google/2cyuw8VBU0No4TQYd (lien de partage Google fourni par Aretro ; liste des jeux : https://portmaster.games/games/).
- **Capture :** à ajouter.

## 5. Need for Speed: Porsche Unleashed

- **Technique :** recompilation / moteur Open-Unleashed (PC).
- **Fichiers requis :** données de la version PC.
- **Portage :** https://github.com/rzrbld/ReNFS5
- **Statut :** le README vise les consoles PortMaster mais a été testé sur une RG40XX-H (muOS) ; il ne cite pas la R36S.
- **Capture :** à ajouter.

## 6. Resident Evil 4 (Mobile / Platinum)

- **Technique :** wrapper qui exécute la version tactile allégée (iOS / Android Platinum).
- **Fichiers requis :** archive IPA (iOS) ou APK/OBB du jeu.
- **Portage :** https://github.com/NextOs-Ports/nextos-universal-ports ou https://github.com/davizerascript/re4-r36s-arkos-beta (README : « R36S/dArkOS PortMaster », bêta).
- **Capture :** à ajouter.

## 7. Zelda: The Wind Waker

- **Technique :** recompilation statique du code GameCube vers ARM64 (sans émulateur Dolphin).
- **Fichiers requis :** ISO GameCube version US.
- **Portage :** distribué par l'équipe NextOS via leur Discord (invitation sur https://github.com/NextOs-Ports/nextos-universal-ports, salon *GameCube port*).
- **Capture :** à ajouter.

## 8. GTA: Vice City

- **Technique :** portage de la version PC (via PortMaster).
- **Fichiers requis :** les fichiers de ta copie PC du jeu.
- **Portage :** officiel PortMaster, fiche « Grand Theft Auto Vice City », par Orson (page « Grand Theft Auto Vice City - Wiki PortMaster » : https://share.google/U7YbiGY3DSJi3qAvp — lien de partage Google, mené vers la fiche ; liste des jeux : https://portmaster.games/games/). La fiche précise : « Vous devez fournir les fichiers du jeu. »
- **Statut :** **fonctionne sur R36S** (constaté par Aretro, 2026-11-17).
- **Capture :** à ajouter.

---

## Hubs

| Hub | Lien | Contenu |
|-----|------|---------|
| Catalogue officiel PortMaster | https://portmaster.games/games/ | Plus de 1 500 portages validés |
| NextOS Universal Ports | https://github.com/NextOs-Ports/nextos-universal-ports | Portages « apporte tes fichiers » pour ArkOS/R36S (38 jeux) |
| Gatito Ports | https://github.com/OlhaGatito/Gatito-Ports | Portages Android/Unity/ARM ; adresse déduite d'un lien tronqué, **non lue** |

## Astuce : centraliser dans PortMaster

Placer `040_nextos.source.json` (dépôt NextOS Universal Ports) dans
`/roms/ports/PortMaster/config/`. Au lancement suivant de PortMaster, leur
catalogue apparaît à côté des portages officiels. (Non testé.)

## Tekken

Pas de recompilation native sur R36S à ce jour : émulation PS1 (Tekken 1 à 3) ou
PSP/PPSSPP (Tekken 5: Dark Resurrection, Tekken 6).

## Captures d'écran

Les images de la réponse Gemini viennent de sites tiers (Moby Games, PlayStation
Blog, Dailymotion…) et ne sont pas libres de droits : elles ne sont pas copiées
ici. Pour illustrer la page, ajouter **tes propres captures prises sur la R36S**
dans `docs/images/r36s/` (ex. `halo.jpg`) et les référencer dans la section du jeu.
