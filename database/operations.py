import psycopg2
from database.connection import conectar_ao_banco

def inserir_dados_no_banco(dados):
    conexao = conectar_ao_banco()
    if conexao is None:
        return

    cursor = conexao.cursor()

    try:
        for item in dados:
            nome = item.get('nome')
            valor = item.get('valor')

            cursor.execute(
                "INSERT INTO dados_api (nome, valor) VALUES (%s, %s)",
                (nome, valor)
            )

        conexao.commit()
        print("Dados inseridos com sucesso!")

    except psycopg2.Error as e:
        print(f"Erro ao inserir dados: {e}")
        conexao.rollback()

    finally:
        cursor.close()
        conexao.close()
