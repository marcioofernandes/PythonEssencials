""" Classe <set> 
- Conjuntos são coleções de itens não ordenados e não indexados.
- Em Python, os conjuntos são escritos com chaves {}.
- Conjuntos não aceitam elementos repetidos.
- Os itens em um conjunto não são acessados por meio de um índice, então não é possível acessar um item de um conjunto usando seu índice.
- Os itens de um conjunto não são ordenados, então a ordem em que os itens foram inseridos não é necessariamente a ordem em que são impressos.
- Uma vez que um conjunto é criado, você não pode alterar seus itens, mas pode adicionar novos itens.
- Para excluir um conjunto, use a instrução del.  """

# Exemplo 1: Criando um conjunto
c1 = {16, 8 , 56, 74, 98}
print (type(c1))

# Exemplo 2: Criando um conjunto vazio com o construtor set ()
c2 = set () 

# Exemplo 3: O contrutor set aceita apenas 1 argumento / ou você pode passar uma lista como argumento
c3 = set ([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

# Exemplo 4: metódos de manipulação de um conjunto 

c = set ()
c.add (26) # adiciona um elemento ao conjunto
c.copy () # retorna uma cópia do conjunto
c.discard (26) # remove o elemento especificado do conjunto
c.update ([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) # adiciona vários elementos ao conjunto
c.pop () # remove um elemento aleatório do conjunto
c.remove (2) # remove o elemento especificado do conjunto
c.clear () # remove todos os elementos do conjunto

# Exemplo 5: Operações com conjuntos
c1 = {1, 2, 3, 4, 5}
c2 = {4, 5, 6, 7, 8}

c1.difference (c2) # retorna um conjunto contendo os elementos de c1 que não estão em c2
c1.difference_update (c2) # remove os elementos de c2 de c1
c1.intersection (c2) # retorna um conjunto contendo os elementos que estão em ambos os conjuntos
c1.intersection_update (c2) # remove os elementos que não estão em ambos os conjuntos
c1.isdisjoint (c2) # retorna True se nenhum elemento estiver presente em ambos os conjuntos
c1.issubset (c2) # retorna True se todos os elementos de c1 estiverem presentes em c2
c1.issuperset (c2) # retorna True se todos os elementos de c2 estiverem presentes em c1 
7 in c2 # retorna True se um elemento específico estiver presente no conjunto
c1.union (c2) # retorna um conjunto contendo os elementos de ambos os conjuntos
c1.symmetric_difference (c2) # retorna um conjunto contendo todos os elementos que não estão presentes em ambos os conjuntos
c1.symmetric_difference_update (c2) # remove os elementos que estão presentes em ambos os conjuntos e insere os elementos que não estão presentes em ambos os conjuntos
c1.update (c2) # insere os elementos de c2 em c1
c3 = frozenset ((1, 2, 3, 4, 5)) # cria um conjunto imutável

"""Exemplos práticos """

print ('Primeira execução')
conjunto = {10, 46,8.8, 64, 98} # criando um conjunto
for c in conjunto:
    print (c) 

print ('Segunda execução')
conjunto = {10,64,46,8.8,98} # criando um conjunto
for c in conjunto:
    print (c) 

"""-------------------------------------------------------------------"""

from random import randint
qtd = int (input ('Quantos números deseja gerar? '))
while qtd > 50:
    qtd = int (input ('Quantidade inválida. Digite um número menor que 50: ')) # validação para não entrar em looping infinito
conjunto = set ()
while len (conjunto) < qtd:
    conjunto.add (randint (1, 50))
print (conjunto)
print (f'Foram gerados {len (conjunto)} números')
