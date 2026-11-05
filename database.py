import sqlite3
connexion=sqlite3.connect("environment.db")
curseur= connexion.cursor()
curseur.execute(""" CREATE TABLE IF NOT EXISTS mesures (
	id INTEGER PRIMARY KEY  AUTOINCREMENT,
	date_heure TEXT,
	temperature REAL,
	humidite REAL,
	pression REAL
)""")
curseur.execute("""
CREATE TABLE IF NOT EXISTS alertes (
	id INTEGER PRIMARY KEY AUTOINCREMENT,
	date_heure TEXT,
	message TEXT
)
""")
connexion.commit()
connexion.close()
print("base de données crée")
