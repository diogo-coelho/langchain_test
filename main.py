from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
import os

load_dotenv()
api_key = os.getenv("API_OPEN_AI_TEST_KEY")

numero_dias = 7
numero_criancas = 2
atividade = "aventura ao ar livre"

prompt = f"Crie um roteiro de viagens no Brasil, para um período de {numero_dias} dias, para uma família com {numero_criancas} crianças, que busca atividades relacionadas a {atividade}."

modelo = ChatOpenAI(
  model="gpt-4o-mini",
  temperature=0.5,
  api_key=api_key
)

resposta = modelo.invoke(prompt)
print(resposta.content)