import requests
from utils.config import API_URL,API_KEY,API_USER,API_APP

def buscar_dados_da_api():
    headers = {
        'Accept': 'application/json',
        'Authorization-Token': API_KEY,  # API_KEY representa o token que você tem
        'User': API_USER,                # API_USER representa o usuário
        'App': API_APP                   # API_APP representa o app (neste caso, 'api')
    }
    
    try:
        response = requests.get(f"{API_URL}/request/Pedidos/GetTodosPedidos?page=0", headers=headers)
        response.raise_for_status()
        dados = response.json()
        return dados
    except requests.exceptions.RequestException as e:
        print(f"Erro ao fazer requisição: {e}")
        return None