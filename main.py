from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()
api_key = os.getenv("API_OPEN_AI_TEST_KEY")

numero_dias = 7
numero_criancas = 2
atividade = "aventura ao ar livre"

prompt = f"Crie um roteiro de viagem de {numero_dias} dias, para uma família com {numero_criancas} crianças, que gosta de {atividade}"


cliente = OpenAI(api_key=api_key)

resposta = cliente.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {"role": "system", "content": "Você é um assistente de viagem."},
        {"role": "user", "content": prompt }
    ])

print(resposta)