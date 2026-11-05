from flask import Flask, render_template
import sqlite3
app= Flask(__name__)
@app.route("/")
def accueil():
	connexion=sqlite3.connect("environment.db")
	curseur=connexion.cursor()
	curseur.execute("""
		SELECT*
		FROM mesures
		ORDER BY id DESC
		LIMIT 1
	""")
	mesure=curseur.fetchone()
	curseur.execute("""
		SELECT date_heure, temperature, humidite, pression
		FROM mesures
		ORDER BY id ASC
	""")
	historique= curseur.fetchall()
	connexion.close()
	return render_template("index.html",mesure=mesure,historique=historique)
app.run(host="0.0.0.0", port=5000)
