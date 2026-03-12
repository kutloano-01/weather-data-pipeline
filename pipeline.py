import requests
import pandas as pd
import psycopg2

# API URL
url = "https://api.open-meteo.com/v1/forecast?latitude=-26.20&longitude=28.04&current_weather=true"

response = requests.get(url)
data = response.json()

weather = data["current_weather"]

# Convert to DataFrame
df = pd.DataFrame([weather])

# Connect to PostgreSQL
conn = psycopg2.connect(
    dbname="weather_db",
    user="postgres",
    password="YOUR_PASSWORD",
    host="localhost",
    port="5432"
)

cursor = conn.cursor()

# Insert data
cursor.execute(
    """
    INSERT INTO weather_data (temperature, windspeed, winddirection, weathercode, time)
    VALUES (%s, %s, %s, %s, %s)
    """,
    (
        weather["temperature"],
        weather["windspeed"],
        weather["winddirection"],
        weather["weathercode"],
        weather["time"]
    )
)

conn.commit()

cursor.close()
conn.close()

print("Weather data inserted into PostgreSQL!")