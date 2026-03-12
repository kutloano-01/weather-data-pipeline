# Weather Data Pipeline

## Project Overview
This is a beginner project built to practice concepts in Data Engineering using Python.

The project creates a simple data pipeline that collects real-time weather data from an API, processes the data, and stores it in a structured format.

The pipeline demonstrates the basic **ETL (Extract, Transform, Load)** process used in many real-world data engineering systems.

## Technologies Used
- Python
- Pandas
- Requests
- Open-Meteo API

## How the Pipeline Works

1. **Extract**
   - The pipeline retrieves weather data (temperature, wind speed/direction, weather code, time) from the Open-Meteo API.
   - Supports default cities or user-input cities at runtime

2. **Transform**
   - The data is cleaned and converted into a structured format using pandas.

3. **Load**
   - The processed data is saved into a CSV file for storage and analysis.
   - Stores data in PostgreSQL (weather_data table)

## Project Structure
```
weather-data-pipeline
│
├── pipeline.py
├── requirements.txt
└── README.md
```

## Installation

Clone the repository:
git clone https://github.com/yourusername/weather-data-pipeline.git


Navigate to the project folder:
cd weather-data-pipeline

Create and activate a virtual environment
python -m venv venv
.\venv\Scripts\Activate.ps1

Install the required packages:
python -m pip install -r requirements.txt


## Usage

Run the pipeline with:
python pipeline.py


After running the script, a file called `weather_data.csv` will be created containing the weather data.

## Future Improvements
This project can be expanded by adding:

- Storing the data in a database like PostgreSQL
- Automating the pipeline to run daily
- Collecting weather data from multiple cities
- Building a dashboard to visualize the data
- Using tools like Apache Airflow for pipeline scheduling

## Learning Goals
The goal of this project is to learn the foundations of Data Engineering, including:

- Working with APIs
- Processing data with Python
- Understanding ETL pipelines
- Storing and managing data
