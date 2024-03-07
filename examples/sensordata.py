import json
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

# Function to write sensor data to a JSON file
def write_to_json(data):
    with open('sensor_data.json', 'w') as json_file:
        json.dump(data, json_file, indent=4)

# Main function
def main():
    while True:
        sensor_data = generate_sensor_data()
        write_to_json(sensor_data)
        print("Dummy sensor data generated and saved to sensor_data.json")
        time.sleep(5)  # Change the interval as needed

if __name__ == "__main__":
    main()
