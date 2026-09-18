# KNN // Decision Lab — Première NSI

Support web interactif pour découvrir le **machine learning supervisé** à travers l'algorithme des **k plus proches voisins (KNN)**, avec un positionnement explicite par rapport au programme officiel de Première NSI.

## Intention pédagogique

Le projet ne présente pas KNN comme une « boîte noire ». L'élève suit une progression :

**représenter → mesurer → trier → choisir k → voter → évaluer → coder**

KNN n'est pas une notion explicitement exigible en Première NSI ; le support l'utilise comme terrain d'application pour les tableaux, dictionnaires, fonctions, parcours, tri, traitement de données, tests et raisonnement algorithmique.

## V2 — Decision Lab

La V2 ajoute notamment :

- un parcours de maîtrise en 6 compétences avec progression locale ;
- un exemple entièrement guidé avant le travail autonome ;
- un laboratoire multi-jeux de données : drones, rôles de jeu et **Iris réel** ;
- distances euclidienne et de Manhattan ;
- vote uniforme ou pondéré par la distance ;
- visualisation correcte du voisinage selon la métrique et la normalisation ;
- frontières de décision dynamiques ;
- mode « hypothèse avant réponse » ;
- démonstration interactive du **piège des échelles** ;
- normalisation par z-score ;
- protocole rigoureux **apprentissage / validation / test** sur Iris ;
- courbe de précision selon k ;
- matrice de confusion sur le jeu de test ;
- exercice de reconstruction du code Python ;
- entraînement mixte avec feedback explicatif et carte de maîtrise ;
- accessibilité clavier, mode clair/sombre et respect de `prefers-reduced-motion`.

## Ressources

- `index.html` — application complète ;
- `assets/iris_2d.csv` — les 150 iris, avec longueur et largeur de sépale ;
- `assets/knn_a_completer.py` — exercice Python sans bibliothèque de machine learning ;
- `.github/workflows/pages.yml` — déploiement GitHub Pages.

## Références principales

- Programme officiel NSI Première — Bulletin officiel spécial n°1 du 22 janvier 2019
- scikit-learn — KNeighborsClassifier et exemple Nearest Neighbors Classification
- CAST Universal Design for Learning Guidelines 3.0
- WCAG 2.2

## Déploiement

Le dépôt est prévu pour être servi par GitHub Pages via GitHub Actions.

Site : https://darksathili-jpg.github.io/knn/
