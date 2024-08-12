"""
Nesse programa, usarei POO, Estrutura de Dados e SQL para registrar e ler os registros de um estoque, incluirei persistencia de dados com txt
Feito por Pedro Henrique
"""

from Produto import Produto
import mysql.connector as mysql
import DAO

def main():
  print("Bem vindo ao sistema de Cadastro de Produtos")
  answer = 0
  produtosCadastrados = []
  try:
    arquivo = open("registros.txt","x")
    arquivo.write("Nome : Valor : Descricao : Categoria : Codigo\n")
  except(FileExistsError):
    arquivo = open("registros.txt","at")
    
  connection = connectToDB("localhost","root","pedro123","estoque")
  
  while(answer != 5):
    answer = int(input("""O que deseja Fazer ?\n1.Cadastro de Produto\n2.Consultar Produtos Cadastrados\n3.Remover Produto \n5.Encerrar\n"""))
    match answer:
      case 1:
        nome = input("Digite o nome do Produto: ")
        precoUnitario = float(input("Digite o preco do Produto: ")).__round__(2)
        descricao = f"Esse produto eh: {nome} de valor {precoUnitario}$"
        categoria = input("Digite a categoria: ")
        novoProduto = Produto(nome,descricao,precoUnitario,categoria)
        print(novoProduto.__str__())
        
        if nome and precoUnitario and descricao and categoria is not None:
          produtosCadastrados.append(novoProduto)
          DAO.insertDB(produto= novoProduto, connection= connection)
          arquivo.write(novoProduto.__str__()+"\n")
        
        pass
      case 2:
        tipoConsulta = input("""Deseja consultar por: 
                            nome = a, 
                            preço = b
                            categoria = c ?\n""")
        match tipoConsulta:
          case 'a':
            res = DAO.consultByName(nome = input("Nome: ").lower(),connection= connection)
            print(f"{res[0]} : {res[1]} : {res[2]} : {res[3]} : {res[4]}")
            pass
          case 'b':
            precoRef = input("Digite um preco medio no formato $$$.$$ : ")
            op = input("Digite a operacao [<(menor) , >(maior) , <= , >=, =] : ")
            res = DAO.consultByPrice(operacao = op ,valor = float(precoRef),connection= connection)
            
            if len(res) > 0:
              for item in res:
                print(item)
            else:
              print("Não foi encontrado nehum resultado")
            
        pass
      case 3:
        pass
      case 4:
        pass
      case 5:
        print("Sistema Encerrado")
        pass
      
def connectToDB(host,user,password,databse):
  
  connection = mysql.connect(
    host=host,
    user=user,
    password=password,
    database=databse
  )
  print(connection)
  
  return connection

if __name__ == "__main__":
  main()