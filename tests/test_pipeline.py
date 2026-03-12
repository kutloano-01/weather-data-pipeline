import unittest
import requests
import psycopg2
import os

class TestWeatherPipeline(unittest.TestCase):

    # API fetch returns weather data
    def test_api_fetch(self):
        url = "https://api.open-meteo.com/v1/forecast?latitude=-26.20&longitude=28.04&current_weather=true"
        response = requests.get(url)
        data = response.json()
        self.assertIn("current_weather", data)
        self.assertIn("temperature", data["current_weather"])


    # Can connect to PostgreSQL
    def test_db_connection(self):
        db_password = os.environ.get("PG_PASSWORD")
        if not db_password:
            self.skipTest("PG_PASSWORD not set, skipping DB test")

        conn = psycopg2.connect(
            dbname="weather_db",
            user="postgres",
            password=db_password,
            host="localhost",
            port="5432"
        )
        cursor = conn.cursor()
        cursor.execute("SELECT 1;")
        result = cursor.fetchone()
        self.assertEqual(result[0], 1)
        cursor.close()
        conn.close()


    # Latitude and longitude are numbers
    def test_coordinates(self):
        lat = -26.20
        lon = 28.04
        self.assertIsInstance(lat, float)
        self.assertIsInstance(lon, float)

if __name__ == "__main__":
    unittest.main()