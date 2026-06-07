# weather_api.py

import requests


def get_coordinates(city):
    url = "https://geocoding-api.open-meteo.com/v1/search"

    response = requests.get(
        url,
        params={"name": city, "count": 1}
    )

    data = response.json()

    if "results" not in data:
        raise ValueError("City not found")

    result = data["results"][0]

    return result["latitude"], result["longitude"]


def get_weather(city):
    lat, lon = get_coordinates(city)

    response = requests.get(
        "https://api.open-meteo.com/v1/forecast",
        params={
            "latitude": lat,
            "longitude": lon,
            "daily": "temperature_2m_max",
            "forecast_days": 7,
            "timezone": "auto"
        }
    )

    return response.json()