import random

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
