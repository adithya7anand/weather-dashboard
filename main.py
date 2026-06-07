# main.py

from weather_api import get_weather
from storage import save_weather
from analysis import analyze, plot_weather


def main():
    city = input("Enter city name: ")

    weather = get_weather(city)

    save_weather(weather, city)

    stats = analyze()

    print("\nWeather Summary")
    print("------------------")
    print("Average:", round(stats["avg_temp"], 2))
    print("Maximum:", stats["max_temp"])
    print("Minimum:", stats["min_temp"])

    plot_weather(city)

    print("\nChart generated successfully")


if __name__ == "__main__":
    main()