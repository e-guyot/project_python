commande d'install pour lancer l'application :
``` pip3 install -r requirements.txt ```
``` pip3 install Pygments ```
``` export FLASK_ENV=development ```
``` python3 nomfichier.py ```


# Partie 1 : enregistrer le langage de programmation utilisé

## python3 sharecode.py

Ajout d'un menu déroulant pour selectionner le language

# Partie 2 : Changez le procédé de stockage, plus de fichiers mais un SGBDR

## python3 sharecodedb.py

Création d'un nouveau model : model_sqlite.py
Ajout création de table codes dans /bdd/create_bdd.py
``` python3 bdd/create_bdd.py ```

# Partie 3 : enregistrez les infos sur les utilisateurs qui publient du code

Ajout création de table users dans /bdd/create_bdd.py
``` python3 bdd/create_bdd.py ```
Ajout de function pour créer user
Ajout du template admin.html


# Partie 4 : colorisation de code


Ajout du fichier functions