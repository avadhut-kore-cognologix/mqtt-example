import random
import time

# Function to generate dummy sensor data
def generate_sensor_data():
    sensor_data = {
        "timestamp": int(time.time()),
        "temperature": round(random.uniform(10.0, 40.0), 2),  # Temperature in Celsius
        "humidity": round(random.uniform(30.0, 90.0), 2),     # Humidity in percentage
        "wind_speed": round(random.uniform(0.0, 20.0), 2),    # Wind speed in meters per second
        "proximity": random.randint(0, 100)                  # Proximity sensor value
    }
    return sensor_data
