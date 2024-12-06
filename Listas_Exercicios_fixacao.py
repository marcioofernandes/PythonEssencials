# Listas 

p = 4 #varial p
r = 3 #varial r 
qtd = 8 #variavel qtd 
termos = [] #lista vazia 
a = 0 # variavel a 

while a < qtd: #enquanto a variavel A for menor que a variavel QTD 
    termos.append (p) #adiciona a variavel P na lista 
    p = p + r # faz a soma de P + R e grava por cima da variavel P ex: 4 + 3 = 7, agora a variavel P é 7 
    a = a + 1 # A variavel A, somada mais 1 
    #o looping se repete até A ser menor que qtd 

print ("\nLista\n")
print (termos)   
print ('\nFim do Programa\n')

""" comando For com lista """

N = int(5)
L = []
for i in range (N): 
    x = float (input(f" elemento {i}: "))
    L.append (x) 
print ("\nResultado")

for valor in L: 
    print (f"{valor:.2f}")
