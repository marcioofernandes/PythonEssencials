# Listas: 
# Tuplas: 
# Sets: 
# Dicionários:

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