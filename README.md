# Gestion de tournoi d'échecs
Logiciel software pour gérer hors ligne et en console un tournoi d'échecs

## A- Pour utiliser le logiciel de gestion de tournois 
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

## B- Pour afficher le peluchage du code avec flake8
### 1- Faire l'étape A au moins jusqu'au 3ème point inclus
### 2- Lancer flake8
    $ flake8 --format=html --htmldir=flake-report
### 3- Ouvrir le dossier flake8-report qui vient de se créer et lancer le "index.html"

# Manage chess_tournament
Software to manage offline and in console chess tournament.

## A- To use the tournament management software 
### 1- Create a folder and place yourself in that folder
    $ with linux :
    $ mkdir <mon_dossier>
    $ cd <mon_dossier>
### 2- Clone "P4_chess_tournament" using git clone.
    $ git clone https://github.com/AnaisG14/P4_chess_tournament.git
### 2- Create and activate a virtual environment (whith linux):
#### -> Placez vous dans le dossier cloné puis
    $ python3 -m venv <environnement name>
    $ exemple: python3 -m venv env
#### -> Activate your virtual environment
    $ source <environnement_name>/bin/activate
    $ exemple : source env/bin/activate

### 3- Install the necessary packages :
    $ pip install -r requirements.txt

### 4- Launch the script :
    $ python3 -m tournchess

## B- To display linting with flake8
### 1- Do step A at least up to the 3rd point included
### 2- Launch flake8
    $ flake8 --format=html --htmldir=flake-report
### 3- Open flake8-report and launch "index.html"

