import requests
from utils.config import API_URL

def buscar_dados_da_api():
    try:
        response = requests.get(API_URL)
        response.raise_for_status()
        dados = response.json()
        return dados
    except requests.exceptions.RequestException as e:
        print(f"Erro ao fazer requisição: {e}")
        return None