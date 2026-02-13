import requests
import os
import string
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("API_KEY")

BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

def get_weather(city: str):
    params = {
        "q": city,
        "appid": API_KEY,
        "units": "metric",
        "lang": "pt_br"
    }

    response = requests.get(BASE_URL, params=params)

    if response.status_code == 404:
        return None

    if response.status_code != 200:
        return None

    return response.json()


def detect_intent(text: str):
    text = text.lower()

    keywords = ["tempo", "clima", "temperatura", "graus", "chover"]

    if any(word in text for word in keywords):
        intent = "weather_current"
    else:
        intent = "unknown"

    city = None
    if "em " in text:
        city = text.split("em ")[-1].strip()
        city = city.strip(string.punctuation)

    return intent, city
