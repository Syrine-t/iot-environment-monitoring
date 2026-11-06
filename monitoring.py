import os
import sqlite3
from datetime import datetime
import board
import busio
import time
import adafruit_bme280.basic as adafruit_bme280
import paho.mqtt.client as mqtt
#initialisation de la communication I2C
i2c = busio.I2C(board.SCL, board.SDA)
#fonction pour detecter le capteur
def detecter_capteur():
	while True:
		try:
			capteur = adafruit_bme280.Adafruit_BME280_I2C(i2c, address=0x76)
			print("Capteur BME280 detecté")
			return capteur
		except (ValueError,OSError) as erreur:
			print(f"Capteur non detecté :{erreur}")
			print("Nouvelle tentative dans 5secondes")
			time.sleep(5)
#Detection initiale du capteur
sensor =detecter_capteur()
#Connexion a la base de données SQLite
connexion =sqlite3.connect("environment.db")
curseur=connexion.cursor()
#config MQTT
client =mqtt.Client()
client.username_pw_set(
	os.environ["MQTT_USERNAME"],
	os.environ["MQTT_PASSWORD"]
)
client.connect("localhost",1883,60)
#boucle de surveillance
alerte_active=False
while True:
	try:
		temp=sensor.temperature
		humidite=sensor.humidity
		pression=sensor.pressure
	except OSError as erreur:
		print(f"Erreur de lecture du capteur: {erreur}")
		print("Nouvelle tentative dans 5secondes")
		time.sleep(5)
		sensor=detecter_capteur()
#on recommence la boucle sans enregister les mesures	
		continue
	

	date_heure= datetime.now().strftime("%Y-%m-%d %H:%M:%S")
	curseur.execute("""
	INSERT INTO mesures
	(date_heure, temperature , humidite , pression)
	VALUES(?,?,?,?)
	""", (date_heure, temp , humidite , pression))
	connexion.commit()
#publication des mesures par MQTT
	client.publish("iot/temperature", f"{temp:.2f}")
	client.publish("iot/humidite", f"{humidite:.2f}")
	client.publish("iot/pression", f"{pression:.2f}")
	print(
		f"{date_heure} | "
		f"Temperature : {temp:.2f} °c | "
		f"Pression: {pression:.2f} hpa |"
		f"Humidité: {humidite:.2f} % |"
	)
	if temp>27 and not alerte_active:
		message="La temperature est superieur a 27°C"
		print(message)
		curseur.execute("""
			INSERT INTO alertes (date_heure,message)
			VALUES(?,?)
		""",(date_heure,message))
		connexion.commit()
		alerte_active=True
	elif temp<= 27:
		alerte_active=False
	time.sleep(10)


