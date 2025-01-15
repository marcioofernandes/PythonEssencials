""" O que são tuplas?

- Tuplas são uma estrutura de dados em Python que permitem armazenar múltiplos itens em uma única variável. 
 Elas são semelhantes às listas, mas com uma diferença crucial: tuplas são imutáveis. 
 Isso significa que, uma vez criada, você não pode alterar, adicionar ou remover itens de uma tupla.

 - Você pode criar uma tupla usando parênteses () e separando os itens por vírgulas."""

# Criando uma tupla
minha_tupla = (1, 2, 3, 4, 5)
print(minha_tupla)

# Acessando itens de uma tupla
print (minha_tupla[0]) # Saída: 1

# ou pode acessar da seguinte forma: 
primeiro_elemento = minha_tupla[0]
print(primeiro_elemento)  # Saída: 1

ultimo_elemento = minha_tupla[-1]
print(ultimo_elemento)  # Saída: 5

# Tentando alterar um item de uma tupla
minha_tupla[0] = 10  # Erro: 'tuple' object does not support

# Concatenando tuplas
tupla1 = (1, 2, 3)
tupla2 = (4, 5, 6)
tupla3 = tupla1 + tupla2
print(tupla3)  # Saída: (1, 2, 3, 4, 5, 6)

# Tuplas aninhadas
tupla_aninhada = (1, 2, (3, 4, 5), (6, 7, 8))
print(tupla_aninhada)  # Saída: (1, 2, (3, 4, 5), (6, 7, 8))

# Desempacotamento de tuplas
tupla = ('Python', 'Java', 'C++')
linguagem1, linguagem2, linguagem3 = tupla
print(linguagem1)  # Saída: Python
print(linguagem2)  # Saída: Java
print(linguagem3)  # Saída: C++

# Ignorando um item
tupla = (1, 2, 3, 4, 5)
primeiro, *meio, ultimo = tupla
print(primeiro)  # Saída: 1
print(meio)  # Saída: [2, 3, 4]
print(ultimo)  # Saída: 5

# Verificando se um item está presente na tupla
tupla = (1, 2, 3)
print(1 in tupla)  # Saída: True
print(4 in tupla)  # Saída: False

# Iterando em uma tupla
tupla = (1, 2, 3)
for item in tupla:
    print(item)
# Saída:
# 1
# 2
# 3

# Encontrando o índice de um item
tupla = (1, 2, 3)
print(tupla.index(1))  # Saída: 0
print(tupla.index(2))  # Saída: 1

# Contando o número de ocorrências de um item
tupla = (1, 2, 2, 2, 3)
print(tupla.count(2))  # Saída: 3

# Encontrando o tamanho de uma tupla
tupla = (1, 2, 3)
print(len(tupla))  # Saída: 3

# Convertendo uma lista em uma tupla
lista = [1, 2, 3, 4]
tupla = tuple(lista)
print(tupla)  # Saída: (1, 2, 3, 4)

# Convertendo uma tupla em uma lista
tupla = (1, 2, 3, 4)
lista = list(tupla)
print(lista)  # Saída: [1, 2, 3, 4]

# Convertendo uma string em uma tupla
string = "Python"
tupla = tuple(string)
print(tupla)  # Saída: ('P', 'y', 't', 'h', 'o', 'n')

