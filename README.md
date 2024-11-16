# Gestion de tournoi d'échecs
Logiciel software pour gérer hors ligne et en console un tournoi d'échecs
# Logiciel de Gestion de Tournois d'Échecs

## Contexte
Un club d'échecs utilise un logiciel de tournoi en ligne qui les a déçu par le passé car trop souvent en panne au moment des tournois. Ils souhaitent donc avoir leur propre logiciel avec un fonctionnement hors ligne.

## Objectifs
Les spécificités du projet étaient les suivantes :
- Fonctionnement hors ligne
- Lancement en ligne de commande (console) et exécutable sur Linux, macOS ou Windows

### Fonctionnalités principales :
1. Créer un nouveau tournoi contenant des caractéristiques personnalisées
2. Maintenir une base de données joueurs avec leurs informations
3. Ajouter des joueurs au tournoi sélectionné
4. Générer des paires de joueurs pour le premier tour
5. Enregistrer les résultats à la fin de chaque tour
6. Générer de nouvelles paires en fonction des résultats
7. Exporter les résultats
8. Sauvegarder les données et reprendre un tournoi plus tard

## Technologies Utilisées
- **Langage :** Python  
- **Base de données légère :** TinyDb  
- **Qualité du code :** Flake8 pour l’analyse statique


## Pour utiliser le logiciel de gestion de tournois 
### 1- Créer un dossier et se placer dans ce dossier.
    $ sous linux :
    $ mkdir <mon_dossier>
    $ cd <mon_dossier>
### 2- Cloner "P4_chess_tournament" en utilisant git clone.
    $ git clone https://github.com/AnaisG14/P4_chess_tournament.git
### 2- Créer et activer un environnement virtuel (sous linux):
#### -> Placez vous dans le dossier cloné puis
    $ python3 -m venv <environnement name>
    $ exemple: python3 -m venv env
#### -> Activer votre environnement virtuel
    $ source <environnement_name>/bin/activate
    $ exemple : source env/bin/activate

### 3- Installer les paquets nécessaires :
    $ pip install -r requirements.txt

### 4- Lancer le script :
    $ python3 -m tournchess

## Pour afficher le peluchage du code avec flake8
### 1- Faire l'étape A au moins jusqu'au 3ème point inclus
### 2- Lancer flake8
    $ flake8 --format=html --htmldir=flake-report
### 3- Ouvrir le dossier flake8-report qui vient de se créer et lancer le "index.html"


## B- To display linting with flake8
### 1- Do step A at least up to the 3rd point included
### 2- Launch flake8
    $ flake8 --format=html --htmldir=flake-report
### 3- Open flake8-report and launch "index.html"

