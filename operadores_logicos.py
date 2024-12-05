# Os operadores lógicos servem para verificar se a condição é verdadeira ou falsa 

a = True
b = False

if a or b: 
    print ("Atendeu a condição")
else: 
    print ("Não atendeu a condição")

# exemplo na prática 

nome = "Marcio"
idade = 35

if nome == "Marcio" and idade == 35: 
    print ("Dados corretos")
else:
    print ("Dados Incorretos")