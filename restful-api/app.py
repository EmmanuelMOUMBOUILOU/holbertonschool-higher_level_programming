# app.py

from flask import Flask

# Créer une instance de l'application Flask
app = Flask(__name__)

# Définir une route de base
@app.route('/')
def home():
    return "Bienvenue sur mon serveur Flask !"

# Démarrer le serveur
if __name__ == '__main__':
    app.run(debug=True)
