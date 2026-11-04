\# IoT Environmental Monitoring System



\## Project Overview



This project consists of an IoT-based environmental monitoring system designed to collect, store, transmit and visualize environmental data using a Raspberry Pi 5.



The system measures temperature, humidity and atmospheric pressure using a BME280 sensor.



\## Hardware



\- Raspberry Pi 5

\- BME280 environmental sensor



\## Technologies



\- \*\*Python:\*\* Sensor data acquisition and processing

\- \*\*I²C:\*\* Communication between the Raspberry Pi and the BME280 sensor

\- \*\*SQLite:\*\* Storage of environmental measurements

\- \*\*Flask:\*\* Development of the web dashboard

\- \*\*HTML / CSS / JavaScript:\*\* Dashboard interface and data visualization

\- \*\*MQTT / Mosquitto:\*\* Real-time data communication with authentication

\- \*\*Linux:\*\* Raspberry Pi operating system



\## System Architecture



BME280 Sensor → Raspberry Pi 5 → Python Application → SQLite Database / MQTT Broker → Flask Dashboard



\## Features



\- Real-time acquisition of temperature, humidity and pressure.

\- Storage of measurements in an SQLite database.

\- Web dashboard for monitoring environmental data.

\- Graphical visualization of measurements.

\- MQTT communication with username/password authentication.



\## Project Status



Core monitoring, database storage, dashboard visualization and authenticated MQTT communication have been implemented and tested.



Automatic startup using systemd and deployment documentation are still in progress.

\## Architecture



The following diagram illustrates the system architecture:



\[View the system architecture](docs/architecture.md)

\## Author



TIC Undergraduate Student

