import psycopg2
from database.connection import conectar_ao_banco

def inserir_dados_no_banco(dados):
    conexao = conectar_ao_banco()
    if conexao is None:
        return

    cursor = conexao.cursor()

    try:
        for item in dados:
            cnpj = item.get('ClienteCNPJ')
            codigo = item.get('Codigo')
            data = item.get('Data')
            validade = item.get('Validade')
            valor_final = item.get('ValorFinal')
            
            codigo = int(codigo)
            cnpj = str(cnpj)
            valor_final = float(valor_final)

            itens = item.get('Items', [])
            quantidade_itens = len(itens)
            for item in itens:
                item_codigo = item.get('Codigo')
                item_descricao = item.get('Descricao')
                quantidade = item.get('Quantidade')

                cursor.execute(
                    """INSERT INTO pedidos (codigo, cnpj, data, validade, valor_final, item_codigo, item_descricao, qtd_items)
                       VALUES (%s, %s, %s, %s, %s, %s, %s, %s)""",
                    (codigo, cnpj, data, validade, valor_final, item_codigo, item_descricao, quantidade_itens,)
                )

        conexao.commit()
        print("Dados inseridos com sucesso!")

    except psycopg2.Error as e:
        print(f"Erro ao inserir dados: {e}")
        conexao.rollback()

    finally:
        cursor.close()
        conexao.close()
