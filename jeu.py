from flask import Flask, render_template, request, redirect, url_for
from unidecode import unidecode
import random
import sqlite3

app = Flask(__name__)

@app.route('/')
def accueil():
    return render_template('accueil.html')

@app.route('/jeu1')
def jeu1():
    conn = sqlite3.connect('fusion.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM fusion")
    fusion = cursor.fetchall()


    # Selectionner un pays aleatoire
    pays_aleatoire = random.choice(fusion)
    conn.close()

    nom_pays = pays_aleatoire[0]
    drapeau = pays_aleatoire[3]

    # Rediriger vers la route de verification avec le nom du pays en tant que parametre
    return render_template('jeu1.html', nom_pays=nom_pays, drapeau=drapeau)

@app.route('/verif1', methods=['POST'])
def verif1():
    nom_pays = request.form['nom_pays']
    capital_saisie = request.form['capitale']
    
    conn = sqlite3.connect('fusion.db')
    cursor = conn.cursor()
    cursor.execute("SELECT CAPITALE FROM fusion WHERE NOM=?", (nom_pays,))
    capital_reel = cursor.fetchone()[0]
    conn.close()

    # Normalisation des chaines de caracteres en enlevant les accents
    capital_saisie = unidecode(capital_saisie)
    capital_reel = unidecode(capital_reel)

    if capital_saisie.lower() == capital_reel.lower():
        resultat = "Correct !"
    else:
        resultat = "Incorrect ! La capitale est " + capital_reel

    return render_template('verif1.html', resultat=resultat)

@app.route('/jeu2')
def jeu2():
    conn = sqlite3.connect('fusion.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM fusion")
    fusion = cursor.fetchall()


    # Sélectionner un pays aleatoire
    pays_aleatoire = random.choice(fusion)
    conn.close()

    nom_pays = pays_aleatoire[0]
    drapeau = pays_aleatoire[3]

    # Rediriger vers la route de verification avec le nom du pays en tant que parametre
    return render_template('jeu2.html', nom_pays=nom_pays, drapeau=drapeau)

@app.route('/verif2', methods=['POST'])
def verif2():
    nom_pays = request.form['nom_pays']
    pays_saisie = request.form['pays']
    
    conn = sqlite3.connect('fusion.db')
    cursor = conn.cursor()
    cursor.execute("SELECT NOM FROM fusion WHERE NOM=?", (nom_pays,))
    pays_reel = cursor.fetchone()[0]
    conn.close()

    # Normalisation des chaines de caracteres en enlevant les accents
    pays_saisie = unidecode(pays_saisie)
    pays_reel = unidecode(pays_reel)

    if pays_saisie.lower() == pays_reel.lower():
        resultat = "Correct !"
    else:
        resultat = "Incorrect ! La pays est " + pays_reel

    return render_template('verif2.html', resultat=resultat)

if __name__ == '__main__':
    app.run(debug=True)
