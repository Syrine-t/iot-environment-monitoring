
# IoT System Architecture

This diagram illustrates the architecture of the IoT Environmental Monitoring System.

```mermaid
flowchart TD
    A["BME280 Environmental Sensor"] -->|"I2C"| B["Raspberry Pi 5"]

    B --> C["Python Monitoring Script"]

    C -->|"Store measurements and alerts"| D[("SQLite Database")]

    C -->|"Publish sensor data"| E["Mosquitto MQTT Broker"]

    D -->|"Retrieve measurements"| F["Flask Web Dashboard"]

    F --> G["HTML / CSS / JavaScript"]
```

## Architecture Components

- **BME280:** Measures temperature, humidity and atmospheric pressure.
- **Raspberry Pi 5:** Processes sensor data.
- **Python:** Reads sensor measurements and manages data transmission.
- **SQLite:** Stores measurements and alerts.
- **Mosquitto MQTT:** Handles authenticated MQTT communication.
- **Flask:** Provides the web dashboard.
- **HTML, CSS and JavaScript:** Build the dashboard interface and visualizations.
