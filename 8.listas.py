""" Listas em Python são coleções ordenadas e mutáveis de itens. 
-Elas permitem armazenar múltiplos valores em uma única variável e são definidas usando colchetes []. 
-Cada item na lista é separado por uma vírgula. 
-Listas podem conter diferentes tipos de dados, incluindo outras listas.

Aqui está um exemplo básico de como criar e manipular listas em Python:"""

# Criando uma lista
minha_lista = ["Maçã", "Banana", "Cereja"]

# Adicionando um item ao final da lista
minha_lista.append("Laranja")

# Inserindo um item em uma posição específica
minha_lista.insert(1, "Manga")

# Removendo o último item da lista
minha_lista.pop()

# Removendo um item por valor
minha_lista.remove("Banana")

# Contando quantas vezes um item aparece na lista
print(minha_lista.count("Maçã"))

# Invertendo a ordem dos itens na lista
minha_lista.reverse()

# Ordenando a lista em ordem alfabética
minha_lista.sort()

# Verificando se um item está na lista
print("Maçã" in minha_lista)

# Extendendo a lista com outra lista
outra_lista = ["Uva", "Pera"]
minha_lista.extend(outra_lista)

# Obtendo o índice de um item
print(minha_lista.index("Cereja"))

# Exibindo a lista final
print(minha_lista)

lista2 = ["guilherme", "bruna"]
lista = ["Marcio", "João", "Maria", "Fernanda"] #sintaxe para criar lista 
lista.append("Lucilene") # Adiciona elemento na lista
lista.insert (2, "Thamires") # adiciona elementa na lista, no lugar desejado 
lista.pop () # Elimina o ultimo elemento da lista - você pode indicar qual elemento retirar 
del lista [1] # Elimina o elemento atribuito no indice correspondente 
lista.remove ("Marcio") # Elimina o elemento através do valor 
lista.count ("Fernanda") # (adicionar o print na frente) conta quantos elementos possui atraves do elemento declarado 
lista.reverse () #inverte a ordem dos elementos em uma lista 
lista.sort () # Organiza os elementos dentro da lista, em ordem alfa-numerica
lista.extend (lista2) # Inclui todos elementos da lista 2 na lista 1 
lista.index ("guilherme") # Retorna o indexador do valor informado 
print ("Marcio" in lista) # verifica se o valor informado contém na lista 

#--------------------------------------------------------------------------------------------------

lista.append ("Jão")
lista.append ("Mariazinha")
lista.append ("Pedro") 
lista.append ("Lucas")
#----------------------------------------------------------------------------------------------------

#Fatiamento de Lista 

sublista = lista [3:6] #o fatiamento é descrito quando você diz para o programa de onde ele tem que começar e onde deve parar ** lembrando que, o último indice não é incluso, no caso aqui ficaria 3:5 

# Fazendo cópia da lista 

copialista = lista [:]
copia2lista = lista.copy ()
copialista.clear () #limpa todos elementos de dentro da lista 


print (lista)
print (sublista)
print (copialista)