import psycopg2
from utils.config import DB_NAME, DB_USER, DB_PASSWORD, DB_HOST, DB_PORT

def conectar_ao_banco():
    try:
        conexao = psycopg2.connect(
            dbname=DB_NAME,
            user=DB_USER,
            password=DB_PASSWORD,
            host=DB_HOST,
            port=DB_PORT
        )
        return conexao
    except psycopg2.Error as e:
        print(f"Erro ao conectar ao banco de dados: {e}")
        return None
