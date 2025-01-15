""" Herança no Python

Nada mais é, que a possibilidade de herdar funções e caracteristicas de outra classe."""

#Primeiro você tem uma classe criada: 

class carros:
    numero_rodas: 4
    numero_passageiro: 4

    def acelerar (self):
        print ("Acelerando...")
    def frear (self): 
        print ('Freando...')
    def buzinar (self):
        print ('Buzinando...')


#Depois você terá uma classe que irá herdar as caracteristicas da classe anterior, e você pode adicionar mais caracteristicas a ela:

class Uno (carros): #Aqui você está dizendo que a classe Uno irá herdar as caracteristicas da classe carros
    modelo = 'Uno'
    marca = 'Fiat'
    ano = 1992 

#Agora você pode criar um objeto da classe Uno e chamar as funções da classe carros:

uno = Uno()
uno.acelerar()
uno.frear()
uno.buzinar()