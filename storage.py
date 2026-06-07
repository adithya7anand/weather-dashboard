# storage.py

import pandas as pd


def save_weather(data, city):
    df = pd.DataFrame({
        "city": city,
        "date": data["daily"]["time"],
        "temperature": data["daily"]["temperature_2m_max"]
    })

    df.to_csv("data/weather.csv", index=False)