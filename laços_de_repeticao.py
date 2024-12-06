
# FOR 

def envia_email (cliente): 
    print (f"Email enviado para o cliente {cliente}")

lista = ["Marcio", "João", "Maria", "Fernanda"]

for cliente in enumerate (lista): # enumera a lista > enumarate 
    envia_email (cliente)

for i, cliente in enumerate (lista):
    if i == 2: 
        break # ou o comando continue 
    envia_email (cliente)




""" 
    Tenho uma lista com objetos? Executa o FOR. 
    Possuo uma condição que preciso repetir ela, utiliza o WHILE 
"""

# WHILE 

numero = 0 

while numero <=10: 
    if numero == 2: 
        break
    numero = numero + 1 
    print (numero)

