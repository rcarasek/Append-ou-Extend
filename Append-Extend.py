class Produto(object):
  def __init__(eu_mesmo, nome, valor): 
    eu_mesmo.__nome = nome 
    eu_mesmo.__valor = valor 

  def __repr__(eu_mesmo): 
    return "nome:%s valor:%s" % (eu_mesmo.__nome, eu_mesmo.__valor)

  def get_nome(eu_mesmo):   
    return eu_mesmo.__nome

  def get_valor(eu_mesmo): 
    return eu_mesmo.__valor

# from model import Produto

chocolate = Produto("cc", 4.35) 
refrigerante = Produto("rr", 3.75) 
feijao = Produto("ff", 10.5) 
produtos = [chocolate, refrigerante, feijao]

print(produtos)

produto4 = Produto("qq", 4.25) 
produtos.append(produto4)
print(produtos)


produto5 = Produto("55", 9.99) 
produtos.extend([produto5])
print(produtos)


produto_novo1 = Produto("66", 4.5) 
produto_novo2 = Produto("77", 3.0)
produtos_novos = [produto_novo1, produto_novo2]
produtos.append(produtos_novos)
print (produtos)


produto_novo8 = Produto("88", 4.5) 
produto_novo9 = Produto("99", 3.0)
produtos_novos = [produto_novo8, produto_novo9]
produtos.extend(produtos_novos)
print (produtos)

produtos.append(produtos_novos)
print (produtos)