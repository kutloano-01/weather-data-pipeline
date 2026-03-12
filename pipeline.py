import os
import requests
import pandas as pd
import psycopg2
from psycopg2 import sql
import getpass


# read password from environment variable 
db_password = os.environ.get("PG_PASSWORD")
if not db_password:
    # if environment variable is not set, prompt the user
    db_password = getpass.getpass("Enter your PostgreSQL password: ")

# list of cities with latitude and longitude
cities = {
    "Johannesburg": {"lat": -26.20, "lon": 28.04},
    "Cape Town": {"lat": -33.92, "lon": 18.42},
    "Durban": {"lat": -29.86, "lon": 31.02}
}

# connect to PostgreSQL
conn = psycopg2.connect(
    dbname="weather_db",
    user="postgres",
    password=db_password,
    host="localhost",
    port="5432"
)
cursor = conn.cursor()

# loop through each city and insert data
for city_name, coords in cities.items():
    url = f"https://api.open-meteo.com/v1/forecast?latitude={coords['lat']}&longitude={coords['lon']}&current_weather=true"
    response = requests.get(url)
    data = response.json()
    weather = data["current_weather"]

    # Insert data into table
    cursor.execute(
        sql.SQL("""
            INSERT INTO weather_data (city, temperature, windspeed, winddirection, weathercode, time)
            VALUES (%s, %s, %s, %s, %s, %s)
        """),
        (
            city_name,
            weather["temperature"],
            weather["windspeed"],
            weather["winddirection"],
            weather["weathercode"],
            weather["time"]
        )
    )
    print(f"Inserted weather data for {city_name}")

conn.commit()
cursor.close()
conn.close()

print("All data inserted successfully!")