import os
import requests
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("OPENWEATHER_API_KEY")


def get_weather(city):
    if not API_KEY:
        return "Weather API key is not configured."

    if not city.strip():
        return "Please tell me a city name."

    url = "https://api.openweathermap.org/data/2.5/weather"

    params = {
        "q": city,
        "appid": API_KEY,
        "units": "metric"
    }

    try:
        response = requests.get(url, params=params, timeout=10)

        if response.status_code == 401:
            return "The weather API key is invalid."

        if response.status_code == 404:
            return f"I couldn't find the city {city}."

        response.raise_for_status()

        data = response.json()

        temperature = data["main"]["temp"]
        humidity = data["main"]["humidity"]
        condition = data["weather"][0]["description"]
        wind_speed = data["wind"]["speed"]

        fahrenheit = (temperature * 9 / 5) + 32

        return (
            f"The weather in {city} is {temperature:.1f} degrees Celsius "
            f"or {fahrenheit:.1f} degrees Fahrenheit. "
            f"The condition is {condition}. "
            f"Humidity is {humidity} percent, "
            f"and wind speed is {wind_speed} meters per second."
        )

    except requests.exceptions.Timeout:
        return "The weather service took too long to respond."

    except requests.exceptions.ConnectionError:
        return "I couldn't connect to the weather service."

    except requests.exceptions.RequestException:
        return "Sorry, I couldn't retrieve the weather right now."