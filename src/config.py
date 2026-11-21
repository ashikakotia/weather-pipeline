"""Settings for the weather pipeline: which cities to track and which fields to fetch."""

CITIES = [
    {"name": "New York", "latitude": 40.71, "longitude": -74.01},
    {"name": "London", "latitude": 51.51, "longitude": -0.13},
    {"name": "Mumbai", "latitude": 19.08, "longitude": 72.88},
    {"name": "Tokyo", "latitude": 35.68, "longitude": 139.69},
    {"name": "Sydney", "latitude": -33.87, "longitude": 151.21},
]

DAILY_FIELDS = ["temperature_2m_max", "temperature_2m_min", "precipitation_sum"]

FORECAST_URL = "https://api.open-meteo.com/v1/forecast"
ARCHIVE_URL = "https://archive-api.open-meteo.com/v1/archive"