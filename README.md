# 🌤️ Maju - Assistente Virtual de Clima

Maju é uma assistente virtual de clima desenvolvida em Python que consulta dados meteorológicos em tempo real através da API OpenWeather e responde de forma natural e amigável ao usuário.

---

## 🚀 Funcionalidades

- Consulta de temperatura atual por cidade
- Informação sobre condição do céu (chuva, nublado, sol, etc.)
- Umidade do ar
- Respostas naturais e espontâneas
- Tratamento de erro para cidades inválidas
- Testes unitários com pytest
- Estrutura modular organizada

---

## 🗂️ Estrutura do Projeto
Maju/
│
├── main.py
├── open_weather/
│ ├── init.py
│ └── weather_service.py
│
├── chat_response/
│ ├── init.py
│ └── IA_service.py
│
├── tests/
│ ├── init.py
│ └── test_service.py
│
└── requirements.txt

---

## ⚙️ Tecnologias Utilizadas

- Python 3.14
- Requests
- Pytest
- OpenWeather API

---

## 🔑 Configuração

1. Clone o repositório:


git clone <url-do-repositorio>
cd Pocco


2. Crie um ambiente virtual (opcional, mas recomendado):


python -m venv venv
venv\Scripts\activate


3. Instale as dependências:


pip install -r requirements.txt


4. Configure sua chave da OpenWeather API no arquivo `weather_service.py`.

---

## ▶️ Executando o Projeto

python main.py

Exemplo de uso:

Você: Quantos graus está em São Paulo?
Maju: Em São Paulo, a temperatura agora está em 22°C...

---

## 🧪 Executando os Testes

Para rodar os testes unitários:

pytest
Se tudo estiver correto:
2 passed

---

## 🧠 Arquitetura

O projeto foi dividido em camadas:

- `weather_service.py` → Responsável por comunicação com a API
- `IA_service.py` → Responsável pela geração de resposta natural
- `main.py` → Interface de interação com o usuário
- `tests/` → Testes unitários isolando chamadas externas com mocks

---

## 📌 Melhorias Futuras

- Suporte a previsão para múltiplos dias
- Interface gráfica
- Deploy em API REST
- Integração com frontend web
- Detecção automática de localização

---

## 👩‍💻 Desenvolvido por
Julia
