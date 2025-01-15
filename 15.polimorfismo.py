"""                   Polimorfismo 

    Permite que objetos com a mesma classe possam ter comportamentos diferentes. Lembra um pouco o conceito de herança, mas com uma diferença, aqui no 
polimorfismo, os objetos podem ter as mesmas funções, mas com comportamentos diferentes. 

Abaixo terá alguns exemplos para deixar o conceito mais claro. """

# Polimorfismo de classe: 
class animal: 
    def emitir_som(self): 
        print ('Qualquer som...')

class cachorro (animal): 
    def emitir_som(self): # Aqui você está sobrescrevendo a função emitir_som da classe animal
        print ('Au Au')

class gato (animal): 
    def emitir_som(self): # Aqui você está sobrescrevendo a função emitir_som da classe animal
        print ('Miau')

cachorro = cachorro () #Aqui você está criando um objeto da classe cachorro
gato = gato () #Aqui você está criando um objeto da classe gato

cachorro.emitir_som()
gato.emitir_som()

'''-------------------------------------------------------------------------------------------'''

# Polimorfismo de interclasse 

class forma():

    def area(self): 
        pass #Aqui você está criando uma função que não faz nada

class quadrado(forma):

    def __init__(self, lado): #Aqui você está criando um construtor para a classe quadrado
        self.lado = lado #Aqui você está criando uma variavel chamada lado
        

    def area (self):
        return self.lado ** 2
    
quadrado = quadrado(4) #Aqui você está criando um objeto da classe quadrado
area_quadrado = quadrado.area() #Aqui você está chamando a função area do objeto quadrado
print(area_quadrado)

class circulo(forma):

    def __init__(self, raio): #Aqui você está criando um construtor para a classe circulo
        self.raio = raio #Aqui você está criando uma variavel chamada raio
        

    def area (self):
        return 3.14 * (self.raio ** 2)
    
circulo = circulo(5) #Aqui você está criando um objeto da classe circulo
area_circulo = circulo.area() #Aqui você está chamando a função area do objeto circulo
print(area_circulo)

'''-------------------------------------------------------------------------------------------''' 
    
"""                  __init__ 

É um método especial que é chamado quando um objeto é criado. Ele é chamado de construtor. Mas o que ele faz? 

- Permite que você crie atributos iniciais de um objeto. 
- Não retorna nada. 

Para ficar mais fácil de entender, imagina que você está criando um carro, sem o __init__ você teria que criar um objeto separado para cada modelo de carro.
Com o __init__ você cria um parametro que vai receber os atributos no momento da criação do objeto.

Com o exemplo abaixo fica mais fácil de entender: 
"""


# Exemplo 1 sem __init__: 
class Carro:
    pass

# Criar o objeto
meu_carro = Carro()

# Configurar atributos manualmente
meu_carro.marca = "Toyota"
meu_carro.cor = "Vermelho"

# Usar o objeto
print(f"Meu carro é da marca {meu_carro.marca} e é {meu_carro.cor}.")

# Exemplo 2 com __init__:
class Carro:
    def __init__(self, marca, cor):
        self.marca = marca  # Atributo do carro
        self.cor = cor      # Atributo do carro

# Criar o objeto, passando os valores diretamente
meu_carro = Carro("Suzuki", "Verde")

# Usar o objeto
print(f"Meu carro é da marca {meu_carro.marca} e é {meu_carro.cor}.")

# entendeu? nem eu! 







