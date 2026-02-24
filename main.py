from chat_service import weather_response
from weather_service import get_weather, extract_city

if __name__ == "__main__":

    print("Maju: Olá sou a Maju, sua assistente virtual de clima. Como posso ajudar?")

    while True:
        user_input = input("Você: ")

        if user_input.lower() in ["não", "nao", "n", "sair", "exit"]:
            print("Maju: Tudo bem. Qualquer coisa, é só me chamar. Até mais!")
            break

        city = extract_city(user_input)

        if not city:
            print("Maju: Não consegui identificar a cidade. Ex: 'Como está o tempo em Recife?'")
            continue

        data = get_weather(city)

        if not data:
            print("Maju: Não consegui obter dados dessa cidade.")
            continue

        response = weather_response(city, data, user_question=user_input)
        print(f"Maju: {response}")
        print("Maju: Quer saber de mais alguma coisa?")