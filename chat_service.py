import random
import os
from dotenv import load_dotenv
from google.genai import Client

load_dotenv()
API_KEY = os.getenv("API_GEMINI_KEY")

# Cria o cliente
client = Client(api_key=API_KEY)

def gemini_response(prompt: str) -> str:

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )
    return response.text

def weather_response(city, data, user_question):
    temp = data["main"]["temp"]
    desc = data["weather"][0]["description"]
    humidity = data["main"]["humidity"]

    prompt = (
        f"Usuário perguntou: '{user_question}'.\n"
        f"Dados atuais do clima em {city}: "
        f"{temp}°C, céu {desc}, umidade {humidity}%.\n\n"
        "Responda de forma espontânea e amigável.\n"
        "Não use saudações no início (não diga 'Olá' ou 'Oi').\n"
        "Não use markdown.\n"
        "Escreva com espaçamento entre os parágrafo.\n"
    )

    return gemini_response(prompt)

def build_response(city, data):

    temp = data["main"]["temp"]
    desc = data["weather"][0]["description"]
    humidity = data["main"]["humidity"]
    wind = data["wind"]["speed"]

    openings = [
        f"Agora em {city}",
        f"No momento em {city}",
        f"Neste instante em {city}"
    ]

    middle = [
        f"está fazendo {temp}°C com {desc}",
        f"a temperatura é de {temp}°C e o céu está {desc}",
    ]

    endings = [
        f". A umidade está em {humidity}%.",
        f". Ventos a {wind} m/s.",
        "."
    ]

    return random.choice(openings) + " " + random.choice(middle) + random.choice(endings)