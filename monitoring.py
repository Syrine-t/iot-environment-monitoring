import os
import sqlite3
from datetime import datetime
import board
import busio
import time
import adafruit_bme280.basic as adafruit_bme280
import paho.mqtt.client as mqtt
i2c = busio.I2C(board.SCL, board.SDA)
sensor = adafruit_bme280.Adafruit_BME280_I2C(i2c, address=0x76)
connexion =sqlite3.connect("environment.db")
curseur=connexion.cursor()
client =mqtt.Client()
client.username_pw_set(
	os.environ["MQTT_USERNAME"],
	os.environ["MQTT_PASSWORD"]
)
client.connect("localhost",1883,60)
while True:
	temp=sensor.temperature
	humidite=sensor.humidity
	pression=sensor.pressure
	date_heure= datetime.now().strftime("%Y-%m-%d %H:%M:%S")
	curseur.execute("""
	INSERT INTO mesures
	(date_heure, temperature , humidite , pression)
	VALUES(?,?,?,?)
	""", (date_heure, temp , humidite , pression))
	connexion.commit()
	client.publish("iot/temperature", f"{temp:.2f}")
	client.publish("iot/humidite", f"{humidite:.2f}")
	client.publish("iot/pression", f"{pression:.2f}")
	print(
		f"{date_heure} | "
		f"Temperature : {temp:.2f} °c | "
		f"Pression: {pression:.2f} hpa |"
		f"Humidité: {humidite:.2f} % |"
	)
	if temp>27:
		message="La temperature est superieur a 27°C"
		print(message)
		curseur.execute("""
			INSERT INTO alertes (date_heure,message)
			VALUES(?,?)
		""",(date_heure,message))
		connexion.commit()
	time.sleep(10)


