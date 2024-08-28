import mysql.connector as mysql
from classes.Produto import Produto


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

def filterConsult(sortBy : str, connection : mysql.MySQLConnection):
    match sortBy.lower():
        case "nome":
            name = input("Digite o nome do Produto")
            consultByName(name,connection)
            pass
        case "preco":
            precoRef = input("Digite um preco medio no formato $$$.$$ : ")
            op = input("Digite a operacao [<(menor) , >(maior) , <= , >=, =] : ")
            consultByPrice(operacao = op ,valor = float(precoRef),connection= connection)
            
            pass
        case "categoria":
            categoria = input("Digite o nome da categoria: ")
            consultByCategory(categoria, connection)
    
def consultByCategory(categoria : str , connection : mysql.MySQLConnection):
    
    try:
        cursor = connection.cursor()
        query = f"SELECT * FROM produto WHERE categoria = '{categoria.lower()}';"
        cursor.execute(query)
        res = cursor.fetchall()
        
        if len(res) > 0:
                for item in res:
                    print(item)
                else:
                    print("Não foi encontrado nehum resultado")
        
    except Exception as e:  # Captura qualquer exceção e imprime a mensagem
        print(f"Erro ao inserir produto: {str(e)}")
    finally:
        print("Operação encerrada")

def removeProduct(identificador, connection : mysql.MySQLConnection):
    item = f"SELECT FROM produto where id = '{identificador}';"
    query = f"DELETE FROM produto where id = '{identificador}';"
    
    try:
        cursor = connection.cursor()
        cursor.execute(item)
        res = cursor.fetchone()
        cursor.execute(query)
        print(f"Item removido : {res}")
        connection.commit()
    except Exception as e:
        print(e.__str__() + " Erro")
    finally:
        print("Operacao Encerrada.")

def getProducts(connection : mysql.MySQLConnection):
    try:
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM PRODUTO;")
        res = cursor.fetchall()
        if len(res) > 0:
                for item in res:
                    print(item)
                else:
                    print("Não foi encontrado nehum resultado")
    except Exception as e:
        print(e.__str__() + " Erro")
    finally:
        print("Operacao Encerrada")

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
        
        if len(res) > 0:
                for item in res:
                    print(item)
                else:
                    print("Não foi encontrado nehum resultado")
        
    except Exception as e:
        print(e.__str__() + " Erro")
    finally:
        print("Operacao Encerrada")