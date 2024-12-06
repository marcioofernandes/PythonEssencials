"""Usado para criar laços de repetição para usos especificos"""

lista = [21,45,17,28] # Declara a lista
for valor in lista: # "Para" cada "Valor" dentro da "lista"
    print (valor) # Imprime o valor separada at~e finalizar a lista 
    valor = 0 # Você pode indicar mais coisas para ser repetido apõs o comando FOR 
    print (valor)

lista2 = ["Marcio", "Fernanda", "Lucilene", "Thamires"]
for nome in lista2: 
    print (nome)

posicao = 0 

for valor in lista:
    print (f"A posição {posicao} da lista, contém o {valor}")
    posicao += 1 





"""Classe RANGE > gera sequencias numericas em progressao aritmética"""

list (range(4, 20, 3)) # primeiro valor: por onde começar 4, segundo valor: até onde o range vai 20, terceiro valor: de quantos em quantos valores ele vai pular 3 
# range(start, stop, step)




"""compreensão de listas - é um recurso onde você consegue aplicar uma expressão ou função para cada um dos itens de uma lista, retornando assim uma nova lista com os itens alterados. """

numeros = [1, 2, 3, 4, 5]

numeros_dobrados = []
for numero in numeros: 
    numeros_dobrados.append (numero * 2)  #sem compreensão de listas 

print (numeros_dobrados)

def dobro (numero): #função dobro 
    return numero * 2 

numeros_dobrados = [numero * 2 for numero in numeros] #compreensão de lista 

numeros_dobrados = [dobro (numero) for numero in numeros ] # com função dentro 

print (numeros_dobrados)

nomes_maiusculos = [nome.upper() for nome in lista2] 
print (nomes_maiusculos)

nomes_maiusculos = [nome.upper() for nome in lista2 if nome [0] == "M"] #compreensão de lista com condicional 
print (nomes_maiusculos)

# [ empressão + For + Condição (opcional)]