# Importing standard libraries
import random  # For generating random weather data
import datetime  # For getting the current date and time
import time  # For simulating time between data points
import math  # For calculating wind chill
import os  # For interacting with the file system
import logging  # For logging information

# Importing a popular external library
import matplotlib.pyplot as plt  # For visualizing data

# Setup logging configuration
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(message)s')
logger = logging.getLogger()

# Simulate data collection for a single time point
temperature = round(random.uniform(-10, 40), 1)  # Generate temperature in °C
humidity = random.randint(20, 100)  # Generate humidity percentage
wind_speed = round(random.uniform(0, 15), 1)  # Generate wind speed in km/h
wind_chill = round(temperature - (math.sqrt(wind_speed) * 3), 1)  # Simple wind chill calculation

# Log the collected weather data
logger.info(f"Temperature: {temperature}°C, Humidity: {humidity}%, Wind Speed: {wind_speed} km/h, Wind Chill: {wind_chill}°C")

# Visualize the data in a simple bar chart
plt.figure(figsize=(8, 5))
plt.bar(["Temperature (°C)", "Humidity (%)", "Wind Speed (km/h)", "Wind Chill (°C)"], [temperature, humidity, wind_speed, wind_chill])
plt.title("Simulated Weather Data")
plt.ylabel("Values")
plt.show()

# Save weather data to a text file
output_path = "weather_data_single_point.txt"
with open(output_path, "w") as f:
    f.write(f"Temperature: {temperature}°C\n")
    f.write(f"Humidity: {humidity}%\n")
    f.write(f"Wind Speed: {wind_speed} km/h\n")
    f.write(f"Wind Chill: {wind_chill}°C\n")
print(f"Weather data saved to {os.path.abspath(output_path)}")
