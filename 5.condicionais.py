"""Condicionáis classicas no formado IF-ELIF-ELSE"""

numero = int(input("Digite um número: "))
if numero % 2 == 0:
    print("O número é par.")
else:
    print("O número é ímpar.")

# uma condicional completa

PH = float(input("Digite um valor do PH: "))
if PH < 6.0:
    r = 'ácida'
elif PH < 7.0:
    r = " Levemente ácida"
elif PH == 7.0:
    r = "Neutra"
elif PH < 8.0:
    r = "Levemente alcalina"
else: 
    r = 'Alcalina'

print (f"Com PH = {PH} a solução é {r}")

#-----------------------------------------------------------------------------------------------

"""Condicionais Anhinhadas-> São condicionais dentro de condicionais""" 

risco = input ('Digite baixo ou alto para o grau de risco: ')


if risco != "baixo" and risco != "alto":
    print (f"{risco} inválido.\n Digite 'baixo' ou 'alto'")
else:
    valor = float (input ("Digite o valor: ")) 
    if risco == "baixo":
        if valor < 1000.0:
            tipo = 'Poupança'
        else: 
            tipo = 'Renda Fixa' 

    else:
        if valor < 1000.0:
            tipo = "Bitcoins"
        else: 
            tipo = "Ações"

    print (f"Você deve investir em {tipo}")

#-------------------------------------------------------------------------------------------
""" A função match-case funciona parecido com a função if - else, porém com a diferença de que, após inserir
o 'input' a função irá verificar se corresponde ao case 1, caso sim, ela interrompe, caso não, ela 
verifica a conrrespondencia com o case 2, e assim por diante, até chegar no final case _ onde ela para
"""

LL = int (input("Digite o número do seu calçado:  "))

match LL: 
    case 16:
        print ('Bebê')
    case 23: 
        print ( 'Infantil')
    case 29: 
        print ('Infantil Esportivo')
    case 42: 
        print ('Masculino Formal')
    case 52: 
        print ('Feminino Formal')
    case _: 
        print ('Código fornecido inválido')

#outro exemplo: 

n = -1 
while n != 0: 
    n = int(input('Digite um inteiro: '))
    match n: 
        case 1:
            print (' Você digitou um')
        case 2: 
            print ('Voce digitou dois')
        case 3: 
            print ('Voce digitou tres') 
        case _:
            print ('Voce digitou um numero diferente') 


# ----------------------------------------------------------------------------------
"""Inline - IF (condicional de uma linha só) """
# Digamos que possuimos a seguinte condicional 
x = 10
y = 20 

if x>= y:
    print (x)
else: 
    print (y) 

# Se quisermos utilizar a formula if de única linha, podemos escrever da seguinte forma: 

print (x) if x >= y else print (y) 

#---------------------------------------------------------------------------------------

"""Para o formato inline-if é obrigatório o uso do else, mesmo quando o código não há obrigatoriedade"""

Codigos = [103, 117, 121, 135, 161, 189, 200, 204, 216]
Lista = []
print ('Alternativa com if Classico')
for codigo in Codigos: 
    if codigo >= 120 and codigo <= 200:
        Lista.append (codigo)
print (f'   códigos filtrados -> {Lista}') 

print ('\nAlternativa com inline-if')
Lista2 = []
for codigos in Codigos: 
    Lista2.append (codigos) if codigos >= 100 and codigos <= 150 else 0 
print (f'  códigos filtrados -> {Lista2}')

#------------------------------------------------------------------------------

"""Outra caracteristica do inline-if é que ele produz um retorno de valor, ou seja, voce pode escrever uma linha de código com a seguinte forma"""

# <Objeto> = <comando True> IF <condição> Else <comando False> : Exemplo abaixo 

B = int(input( 'Digite um numero inteiro: '))
paridade = 'Par' if B % 2 == 0 else 'Impar'
print (f'O valor {B} é {paridade}')

