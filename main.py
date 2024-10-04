from api.api_service import buscar_dados_da_api
from database.operations import inserir_dados_no_banco

if __name__ == '__main__':
    dados = buscar_dados_da_api()
    
    if dados:
        inserir_dados_no_banco(dados)
    else:
        print("Nenhum dado foi encontrado na API.")
