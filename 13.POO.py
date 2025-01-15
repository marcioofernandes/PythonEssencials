"""                                    Programação orientada a objetos (POO)

- O que são classes? 
Classes são modelos para criar objetos. Dentro de uma classe você pode definir funções e variaveis que serão utilizadas no objeto. 

- O que são objetos?
Objetos são instancias de classes. Ou seja, quando você cria um objeto, você está criando uma instancia de uma classe. Ficou confuso? 

- Deixa eu explicar melhor: 
O objeto é como se fosse um bolo em si, e a classe seria a receita desse bolo. 

... agora abaixo temos um exemplo de uma classe e um objeto: 

"""

class Celular: #Aqui você está criando uma classe chamada Celular
    marca = 'Nokia'
    modelo = 'Tijolão'
    cor = 'Azul'
    tem_camera = False
    bateria = 'Infinita'

    def fazer_ligação(self):
        print('Fazendo ligação...')
    
    def jogar_cobrinha (self):
        print('Jogando cobrinha...')

    def despertador (self): 
        print('Despertador ativado...')

    def calcular (self, v1, v2):
        return v1 + v2 

celular = Celular() #Aqui você está criando um objeto da classe Celular

print (celular.calcular(45,55)) 

#ou 

calculado = celular.calcular(45,55)
print(calculado) 


