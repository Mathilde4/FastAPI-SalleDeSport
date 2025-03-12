Learning FastAPI

Ce projet est une API développée avec FastAPI, utilisant Mysql comme base de données. Il permet de gérer une salle de sport. L'utilisation d'une  doumentation claire et élaborée

Fonctionalités : 

Gestion des clients (ajout, modification, suppression, liste)
Gestion des packs (ajout, modification, suppression, liste)
Gestion des abonements (ajout, modification, suppression, liste)
Authentification des utilisateurs avec JWT
Import d'un fichier pdf concernant les différentes transactions effectuées

Installation : 

-Cloner le projet : 
git clone https://github.com/Mathilde4/Learning-FastAPI.git
cd Learning-FastAPI

-Créer un environnement virtuel(Optionnel mais recommandé) :
python -m venv env
Sur Windows : env\Scripts\activate.bat

_Installer les dépendances : 
pip install -r requirements.txt

-Lancer le projet : 
uvicorn item.main:app --reload

_Tester l'api : 
utiliser Swagger ui : http://127.0.0.1:8000/docs
Utiliser Postman ou cURL pour tester les endpoints.

Technologies utilisées : 
Backend : FastAPI, SQLAlchemy
Base de données : Mysql
Authentification : OAuth2, JWT


Auteur : 
👨‍💻 Mathilde
📧 Contact : mathibassadou@gmail.com




