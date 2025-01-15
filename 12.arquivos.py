'''          TRABALHAR COM ARQUIVOS

É muito comum quando você precisa salvar, ler ou manipular dados em formatos como txt, CSV, JSON entre outros. 
Arquivos podem ser usados para armazenar informação que permacem disponiveis mesmo após o programa ser encerrado. 

 - Para manipular arquivos em Python usa-se a função open() que recebe dois argumentos: o nome do arquivo e o modo de abertura.

    - O modo de abertura pode ser:
        - 'r' : leitura
        - 'w' : escrita
        - 'a' : adição
        - 'r+' : leitura e escrita
        - 'b' : modo binário
        - 'x' : criação
        - 't' : modo texto

    - Exemplo: 
        - arquivo = open('arquivo.txt', 'r')
        - arquivo = open('arquivo.txt', 'w')
        - arquivo = open('arquivo.txt', 'a')
        - arquivo = open('arquivo.txt', 'r+')
        - arquivo = open('arquivo.txt', 'b')
        - arquivo = open('arquivo.txt', 'x')
        - arquivo = open('arquivo.txt', 't')

- Para fechar um arquivo usa-se o método close().

abaixo será realizado uma série de exemplos de como trabalhar com arquivos em Python. '''

# Exemplo 1: Criando um arquivo e escrevendo nele

arquivo = open("exemplo.txt", "w") # Abre o arquivo exemplo.txt em modo de escrita

arquivo.write ("Olá, mundo! \n") # Escrever no arquivo
arquivo.write ("Este é um exemplo de arquivo. \n")

arquivo.close () # Fecha o arquivo 


'''-----------------------------------------------------------------------------------'''

# Exemplo 2: Lendo um arquivo

arquivo = open ("exemplo.txt", "r") # Abre o arquivo exemplo.txt em modo de leitura

conteudo = arquivo.read() # Lê o conteúdo do arquivo
print (conteudo)

arquivo.close () # Fecha o arquivo

''' outros métodos de leitura: 
        - readline() : lê a primeira linha do arquivo
        - readlines() : lê todas as linhas do arquivo e retorna uma lista com elas'''

'''-----------------------------------------------------------------------------------'''

# Exemplo 3: Adicionando conteúdo a um arquivo

arquivo = open ("exemplo.txt", "a") # Abre o arquivo exemplo.txt em modo de adição

arquivo.write ("Nova linha adicionada. \n") # Adiciona uma nova linha ao arquivo

arquivo.close () # Fecha o arquivo

'''-----------------------------------------------------------------------------------'''

# Exemplo 4: Usando With para manipular arquivos (recomendado) - O método close() é chamado automaticamente

with open ("exemplo.txt", "r") as arquivo: 
    conteudo = arquivo.read()
    print (conteudo)


# Exemplos práticos 

''' Enunciado: 
Escreva um programa que permaneça em laço lendo números inteiros até que seja digitado 0.
todos os valores digitados exceto o zero, devem ser gravados em um arquivo em disco, um por linha.'''

arq = open ('exercicio.txt', 'w')
a = int(input('Digite um número: '))
while a != 0:
    arq.write(f'{a}\n')
    a = int(input('Digite um número: '))

arq.close()

''' Enunciado:
Escreva um programa que permaneça em laço lendo números inteiros até que seja digitado 0.
todos os valores digitados exceto o zero, devem ser gravados em um arquivo em disco, um por linha,
com 3 casas decimais.'''

lista = []
x = float(input('Digite um número: '))
while x != 0:
    lista.append(f'{x:.3f}\n')
    x = float(input('Digite um número: '))
arq = open ('exercicio2.txt', 'w')
arq.writelines(lista)
arq.close()

''' Enunciado:
Escreva um programa que permaneça que leia um arquivo de entrada, sabendo que esse arquivo tem um numero inteiro em cada linha.
todos os numeros lidos devem ser mostrados na tela. mostrar tbm a soma dos valores, a quantidade, a média aritmética, o menor valor e o maior valor.'''

lst = []
arquivoEntrada = open ('exercicio.txt', 'r')
linha = arquivoEntrada.readline()
while linha != '':
    lst.append(int(linha))
    linha = arquivoEntrada.readline()
arquivoEntrada.close()

soma = sum(lst)
qtd = len(lst)
media = soma/qtd
menor = min(lst)
maior = max(lst)

print(f'Valores: {lst}')

'''Enunciado: 
Usar o mesmo arquivo de entrada do exercício anterior.
usar um iterador for e o arquivo como iteravel'''

lst = []

for linha in open('exercicio.txt', 'r'):
    lst.append(int(linha)) # esta linha é o mesmo que o começo do exercicio anterior
# o restante é igual 






