from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv
import os

load_dotenv()
api_key = os.getenv("API_OPEN_AI_TEST_KEY")

numero_dias = 7
numero_criancas = 2
atividade = "aventura ao ar livre"

modelo_de_prompt = PromptTemplate(
  template="""
  Crie um roteiro de viagem de {dias} dias no Brasil,
  para uma família com {numero_criancas} crianças,
  que gostam de {atividade}.
  """
)

prompt = modelo_de_prompt.format(
  dias=numero_dias,
  numero_criancas=numero_criancas,
  atividade=atividade
)

print("Prompt : \n", prompt)

modelo = ChatOpenAI(
  model="gpt-4o-mini",
  temperature=0.5,
  api_key=api_key
)

resposta = modelo.invoke(prompt)
print(resposta.content)