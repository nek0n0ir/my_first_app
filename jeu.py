from flask import Flask, render_template, request, redirect, url_for
import random
import sqlite3

app = Flask(__name__)

@app.route('/')
def jouer():
    conn = sqlite3.connect('pays.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM pays")
    pays = cursor.fetchall()


    # Sélectionner un pays aléatoire
    pays_aleatoire = random.choice(pays)
    conn.close()


    nom_pays = pays_aleatoire[0]
    drapeau = pays_aleatoire[3]

    # Rediriger vers la route de vérification avec le nom du pays en tant que paramètre
    return render_template('verifier.html', nom_pays=nom_pays, drapeau=drapeau)

@app.route('/verifier', methods=['POST'])
def verifier():
    nom_pays = request.form['nom_pays']
    capital_saisie = request.form['capitale']
    
    conn = sqlite3.connect('pays.db')
    cursor = conn.cursor()
    cursor.execute("SELECT capitale FROM pays WHERE nom_pays=?", (nom_pays,))
    capital_reel = cursor.fetchone()[0]
    conn.close()

    if capital_saisie == capital_reel:
        resultat = "Correct !"
    else:
        resultat = "Incorrect ! La capitale est " + capital_reel

    return render_template('resultat.html', resultat=resultat)

if __name__ == '__main__':
    app.run(debug=True)
