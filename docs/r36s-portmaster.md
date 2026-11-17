# R36S — portages PortMaster : liens de départ

> **Statut : non vérifié.** Liste recopiée le 2026-11-17 depuis une réponse de
> Gemini (captures d'écran), sans rien tester sur la console et sans avoir
> ouvert les dépôts. Elle sert de **base de départ** à la section PortMaster de
> la fiche `consoles/r36s.json` ; chaque ligne reste à confirmer (dépôt
> existant, jeu qui démarre sur R36S, version d'ArkOS/dArkOS) avant de passer
> en « vérifié ». Aucune ROM, aucun BIOS, aucun fichier de jeu : presque tous
> ces portages demandent les fichiers du jeu que l'on possède (ISO Xbox/GameCube,
> APK/OBB, fichiers PC).

## Hubs qui regroupent des portages

| Hub | Lien | Contenu |
|-----|------|---------|
| Catalogue officiel PortMaster | https://portmaster.games/games | Plus de 1 500 portages validés (ex. *Need for Speed II SE*, *Zelda: A Link to the Past*) |
| NextOS Universal Ports | https://github.com/NextOs-Ports/nextos-universal-ports | Portages non officiels pour R36S (ArkOS/dArkOS) issus d'Android, iOS, GameCube : *Resident Evil 4 Platinum*, *Zelda: Wind Waker* (via leur Discord lié sur le dépôt) |
| Gatito Ports | https://github.com/OlhaGatito/Gatito-Ports | Portages Android/Unity/ARM compatibles R36S et PortMaster (adresse déduite d'un lien tronqué : à confirmer) |

## Portages par jeu

| Jeu | Type de portage | Lien du dépôt / source |
|-----|-----------------|------------------------|
| Halo (Combat Evolved) | Décompilation ARM64 (ISO Xbox requise) | https://github.com/kirklandsig/halo-ce-anbernic-rg35xx (indiqué compatible R36S sous dArkOS/ArkOS via le zip PortMaster) |
| Need for Speed II SE | Officiel PortMaster (fichiers PC) | https://portmaster.games/games (chercher « Need For Speed II SE ») |
| Need for Speed II SE | Recompilation statique PC (v1.0 ou v1.2) | https://github.com/manuelpllull/nfsu2-recompiled-r36s |
| Need for Speed Most Wanted | Wrapper Android (APK + OBB requis) | https://github.com/EapRules/nfsmw-r36s |
| Need for Speed 5 | Recompilation / moteur Open-Unleashed (PC) | https://github.com/rzrbld/ReNFS5 |
| Resident Evil 4 Platinum | Portage mobile/iOS (bêta R36S) | https://github.com/NextOs-Ports/nextos-universal-ports ou https://github.com/davizerascript/re4-r36s-arkos-beta |
| Jeux GameCube (nom non précisé dans la source) | Recompilation GameCube (version US) | Publiée par l'équipe NextOS (lien Discord sur https://github.com/NextOs-Ports/nextos-universal-ports, salon *GameCube port*) |

Remarque : pas de recompilation native de Tekken sur PortMaster pour R36S à ce
jour ; la série passe par l'émulation PS1 (Tekken 1 à 3) ou PSP/PPSSPP
(Tekken 5: Dark Resurrection et Tekken 6).

## Astuce : centraliser les sources dans PortMaster

Récupérer `040_nextos.source.json` dans le dépôt NextOS Universal Ports et le
placer dans `/roms/ports/PortMaster/config/`. Au lancement suivant de
PortMaster sur la console, leur catalogue apparaît à côté des portages
officiels. (Non testé.)
