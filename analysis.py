# analysis.py

import pandas as pd


def analyze():
    df = pd.read_csv("data/weather.csv")

    return {
        "avg_temp": df["temperature"].mean(),
        "max_temp": df["temperature"].max(),
        "min_temp": df["temperature"].min()
    }

import matplotlib.pyplot as plt


def plot_weather(city):
    df = pd.read_csv("data/weather.csv")

    plt.figure(figsize=(8, 4))

    plt.plot(
        df["date"],
        df["temperature"],
        marker="o"
    )

    plt.title(f"Temperature Forecast - {city}")
    plt.xlabel("Date")
    plt.ylabel("Temperature (°C)")
    plt.xticks(rotation=45)

    plt.tight_layout()

    plt.savefig("data/weather_chart.png")