import mysql.connector as mysql
from Produto import Produto


def insertDB(produto: Produto, connection):
    query = "INSERT INTO produto (nome, descricao, preco, categoria, codigo) VALUES (%s, %s, %s, %s, %s);"
    val = (
        produto.getNome(),
        produto.getDescricao(),
        produto.getPrecoUnitario(),
        produto.getCategoria(),
        produto.getCodigo()
    )

    try:
        cursor = connection.cursor()
        cursor.execute(query, val)
        connection.commit()
        print("Operação Concluída")
    except Exception as e:  # Captura qualquer exceção e imprime a mensagem
        print(f"Erro ao inserir produto: {str(e)}")
    finally:
        print("Operação encerrada")
