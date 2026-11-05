# Deployment Guide



## 1. Hardware Requirements



- Raspberry Pi 5

- BME280 environmental sensor

- Jumper wires

- Stable power supply



## 2. Sensor Wiring



| BME280 | Raspberry Pi 5 |

|---|---|

| VIN | 3.3V (Pin 1) |

| GND | GND (Pin 6) |

| SDA | GPIO2 (Pin 3) |

| SCL | GPIO3 (Pin 5) |



## 3. Enable I2C



Enable the I2C interface on Raspberry Pi OS using:



```

sudo raspi-config

```



Select Interface Options, then I2C, and enable it.



Check sensor detection:



```

sudo i2cdetect -y 1

```



The BME280 should appear at address `0x76`.



## 4. Install Python Dependencies



Clone the repository and enter the project directory:



```

git clone https://github.com/Syrine-t/iot-environment-monitoring.git

cd iot-environment-monitoring

```



Install dependencies in a Python virtual environment:



```

python3 -m venv .venv

source .venv/bin/activate

pip install -r requirements.txt

```



## 5. Configure MQTT



Install Mosquitto and its client utilities:



```

sudo apt install mosquitto mosquitto-clients

```



Configure the MQTT broker with authentication.



Store MQTT credentials in a protected environment file. Never publish real credentials to GitHub.



## 6. Initialize the Database



```

python3 database.py

```



This creates the SQLite database tables.



## 7. Run the Application



Start the monitoring script:



```

python3 monitoring.py

```



Start the dashboard in another terminal:



```

python3 app.py

```



Access the dashboard at:



```text

http://RASPBERRY\_PI\_IP:5000

```



## 8. Automatic Startup



The project uses two systemd services:



- `iot-monitoring.service`

- `iot-dashboard.service`



Check their status:



```

sudo systemctl status iot-monitoring.service

sudo systemctl status iot-dashboard.service

```



Both services should be active and running.



