from chat_service import build_response
from weather_service import get_weather, detect_intent

if __name__ == "__main__":
    user_input = input("Pergunte sobre o clima: ")

    intent, city = detect_intent(user_input)

    if intent == "weather_current" and city:
        data = get_weather(city)

        if not data:
            print("Não consegui obter dados dessa cidade.")
        else:
            response = build_response(city, data)
            print(response)
    else:
        print("Eu só respondo perguntas sobre clima. Ex: 'Como está o tempo em Recife?'")
