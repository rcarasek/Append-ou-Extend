class Produto(object):
  def __init__(self, nome, valor): 
    self.__nome = nome 
    self.__valor = valor 

  def __repr__(self): 
    return "nome:%s valor:%s" % (self.__nome, self.__valor)

  def get_nome(self):   
    return self.__nome

  def get_valor(self): 
    return self.__valor

# from model import Produto

chocolate = Produto("Chocolate", 4.35) 
refrigerante = Produto("Refrigerante", 3.75) 
feijao = Produto("Feijao", 10.5) 
produtos = [chocolate, refrigerante, feijao]

print(produtos)

