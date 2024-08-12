from typing import Any
import random

class Produto:
  def __init__(self, nome, descricao, precoUnitario, categoria):
    self.__nome = nome
    self.__categoria = categoria
    self.__codigo = self.createCodigo()
    self.__descricao = descricao
    self.__precoUnitario = precoUnitario
    
  def createCodigo(self):
    return random.randint(1,9999999)
  
  def getNome(self):
    return self.__nome
  
  def getCodigo(self):
    return self.__codigo
  
  def getDescricao(self):
    return self.__descricao
  
  def getPrecoUnitario(self):
    return self.__precoUnitario
  
  def getCategoria(self):
    return self.__categoria
  
  def __str__(self) -> str:
    return f"{self.__nome} : {self.__precoUnitario} : {self.__descricao} : {self.__categoria} : {self.__codigo}"