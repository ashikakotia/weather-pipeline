"""Extract: download daily weather from the Open-Meteo API and turn it into clean rows."""

import logging

import requests

from src.config import CITIES, DAILY_FIELDS, FORECAST_URL

logger = logging.getLogger(__name__)


def fetch_daily(city: dict, past_days: int = 2) -> dict:
    """Call the forecast API for one city and return the JSON as a dict."""
    params = {
        "latitude": city["latitude"],
        "longitude": city["longitude"],
        "daily": ",".join(DAILY_FIELDS),
        "past_days": past_days,
        "forecast_days": 1,
        "timezone": "auto",
    }
    response = requests.get(FORECAST_URL, params=params, timeout=10)
    response.raise_for_status()  # stop with an error on 4xx/5xx instead of failing silently
    return response.json()


def parse_daily(city_name: str, payload: dict) -> list[dict]:
    """Turn the API's column-style JSON into one dict per day."""
    daily = payload["daily"]
    rows = []
    for i, day in enumerate(daily["time"]):
        rows.append(
            {
                "city": city_name,
                "date": day,
                "temp_max_c": daily["temperature_2m_max"][i],
                "temp_min_c": daily["temperature_2m_min"][i],
                "precipitation_mm": daily["precipitation_sum"][i],
            }
        )
    return rows


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    for city in CITIES:
        rows = parse_daily(city["name"], fetch_daily(city))
        logger.info("%s: %d rows", city["name"], len(rows))
        for row in rows:
            print(row)