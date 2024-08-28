"""
Nesse programa, usarei POO, Estrutura de Dados e SQL para registrar e ler os registros de um estoque, incluirei persistencia de dados com txt
Feito por Pedro Henrique
"""

from classes.Produto import Produto
import DAO.DAO_PRODUTO as DAO_PRODUTO
from DAO.DB import DB



def main():
  print("Bem vindo ao sistema de Cadastro de Produtos")
  answer = 0
  produtosCadastrados = []
  try:
    arquivo = open("registros.txt","x")
    arquivo.write("Nome : Valor : Descricao : Categoria : Codigo\n")
  except(FileExistsError):
    arquivo = open("registros.txt","at")
    
  connection = DB.connectToDB("localhost","root","pedro123","estoque")
  
  while(answer != 5):
    answer = int(input("""O que deseja Fazer ?\n1.Cadastro de Produto\n2.Consultar Produtos Cadastrados\n3.Remover Produto \n4.Mostrar todos os produtos\n5.Encerrar\n"""))
    match answer:
      case 1:
        nome = input("Digite o nome do Produto: ")
        precoUnitario = float(input("Digite o preco do Produto: ")).__round__(2)
        descricao = f"Esse produto eh: {nome} de valor {precoUnitario}$"
        categoria = input("Digite a categoria: ")
        novoProduto = Produto(nome,descricao,precoUnitario,categoria)
        print(novoProduto.__str__())
        
        if nome and precoUnitario and descricao and categoria:
          produtosCadastrados.append(novoProduto)
          DAO_PRODUTO.insertDB(produto= novoProduto, connection= connection)
          arquivo.write(novoProduto.__str__()+"\n")
        
        pass
      case 2:
        tipoConsulta = input("""Deseja consultar por: 
                            nome, 
                            preço ou
                            categoria ?\n""")
        DAO_PRODUTO.filterConsult(tipoConsulta,connection)
        
        pass
      case 3:
        # Remover Produto de nossa base de dados
        DAO_PRODUTO.getProducts(connection)
        idToBeRemoved = input("Qual id você deseja remover?")
        DAO_PRODUTO.removeProduct(idToBeRemoved, connection)
        DAO_PRODUTO.getProducts(connection)
        pass
      case 4:
        DAO_PRODUTO.getProducts(connection)
        pass
      case 5:
        print("Sistema Encerrado")
        connection = DB.closeDB()
        pass
      
if __name__ == "__main__":
  main()
