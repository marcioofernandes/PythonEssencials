""" Resumo da Estrutura

Definição de Funções: Começa com def.

Argumentos: Informações que a função usa para funcionar.

Tipos de Argumentos:
Simples, nomeados, variáveis (*), ou palavras-chave (**).

Retorno: Use return para devolver um valor.
"""
# 1. Funções são uma máquina de tarefas, que executa uma ação especifica quando é chamada. 

def diga_ola(): 
    print ("Olá")

diga_ola()
""" -------------------------------------------------------------------------------------------"""
# 2. Funções sem argumentos 

def mostre_boas_vindas (): # São funções que n"ao precisam de informações exernas para funcionar. 
    print ("Bem vindo ao entendimento das funções")

mostre_boas_vindas () 
"""-----------------------------------------------------------------------------------------------"""
# 3. Argumentos Obrigátorios e Opcionais 

# Obrigatórios 

def saudacao (nome): 
    print (f'Olá, {nome}!')

saudacao ("Marcio")

# Argumentos opcionais 

def saudacao (nome="visitante"): #possui valores padrões que podem ser ignorados
    print (f'Olá, {nome}!')

saudacao () 
saudacao ("Fernanda")

"""--------------------------------------------------------------------------------------------------"""
#4. Vários argumentos obrigátórios 

def soma(a, b):
    return a + b

print(soma(5, 3))  # Como usar uma calculadora básica, você precisa de dois numeros para somar 
""" ------------------------------------------------------------------------------------------------------"""

# 5. Funcções como argumentos 

""" Você pode passar uma função como argumento para outra. """

def aplicar_operação (funcao, valor): # cria a função que irá precisar de dois parametros 
    return funcao (valor) # retorna que a função indicada, conterá o valor indicado 

def dobrar (x): #cria outra função que fazer o dobro do numero indicado 
    return x * 2 

print (aplicar_operação (dobrar, 5)) # aqui voce chama a função, que terá como (dobrar, 5) e ai ativa a proxima função que é usar o valor * 2 

"""--------------------------------------------------------------------------------------------------------------"""

# 6. Use argumentos como palavra-chaves 

def pedido_pizza(tamanho, borda):
    print(f"Você pediu uma pizza {tamanho} com borda {borda}.")

pedido_pizza(borda="catupiry", tamanho="grande")

'''-----------------------------------------------------------------------------------------------------------------'''

# 7. Misturando argumentos e arumentos de palavra chave 

''' O conceito é combinar os dois tipos mas os argumentos normais vem primeiro '''

def pizza_pedido(tamanho, borda="normal"):
    print(f"Pizza {tamanho} com borda {borda}.")

pizza_pedido("média")  # Saída: Pizza média com borda normal.
pizza_pedido("grande", borda="recheada")  # Saída: Pizza grande com borda recheada.

'''-------------------------------------------------------------------------------------------------------------------'''

# 8. Argumentos Variáveis 

''' Permite passar qualquer número de argumentos posicionais usando * '''

def soma(*numeros):
    return sum(numeros)

print(soma(1, 2, 3, 4))  # aqui a quantidade de numeros podem variar 

""" ------------------------------------------------------------------------------------------------------------------"""

# 9. Argumentos de Palavras chave variaveis 

''' aceita qualquer número de argumento nomeados usando ** '''

def exibir_informacoes(**dados):
    for chave, valor in dados.items(): # O que aconteceu aqui? 
        print(f"{chave}: {valor}")

exibir_informacoes(nome="Marcio", idade=35, cidade="São Paulo")

"""O que acontece aqui?:

dados.items(): Retorna cada par (chave, valor) do dicionário.
Laço for:
Itera sobre os pares do dicionário.
Em cada iteração:
chave: Recebe a "chave" atual (ex.: "nome").
valor: Recebe o "valor" correspondente (ex.: "Marcio").
print(f"{chave}: {valor}"):
Exibe as chaves e valores no formato chave: valor. 
"""





