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

def consultByName(nome : str, connection : mysql.MySQLConnection):
    query = f"select * from produto where nome = '{nome}'"
    try:
        cursor = connection.cursor()
        cursor.execute(query)
        res = cursor.fetchone()
        print("Operação Concluída")
        return res
    except Exception as e:  # Captura qualquer exceção e imprime a mensagem
        print(f"Erro ao consultar produto: {str(e)}\n")
    finally:
        print("Operação encerrada")

def consultByPrice(operacao : str , valor : float, connection: mysql.MySQLConnection ):
    query = ""
    match operacao:
        case '<':
            query = f"select * from produto where preco < {valor}"
            pass
        case '>':
            query = f"select * from produto where preco > {valor}"
            pass
        case '<=':
            query = f"select * from produto where preco <= {valor}"
            pass
        case '>=':
            query = f"select * from produto where preco >= {valor}"
            pass
        case '=':
            query = f"select * from produto where preco = {valor}"
            pass
        
    try:
        cursor = connection.cursor()
        cursor.execute(query)
        res = cursor.fetchall()
        return res
    except Exception as e:
        print(e.__str__() + " Erro")
    finally:
        print("Operacao Encerrada")