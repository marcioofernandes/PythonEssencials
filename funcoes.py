""" Função é um bloco de código que só é executado quando é chamado. Você pode passar paramentros para uma função.
ARGUMENTOS: são especificados após o nome da função, dentro dos parênteses. (pode adicionar quantos quiser, basta separa-los por virgulas
PARÂMETRO: é a variável listada dentro dos parênteses na definição da função. )"""

def my_function(fname):
  print(fname + " Refsnes")

my_function("Emil") # cada palavra descrita aqui, sera correspondente ao fname
my_function("Tobias")
my_function("Linus")

# ----------------------------------------------------------------------------------------------------------------------

def my_function(fname, lname): #dois argumentos
  print(fname + " " + lname)

my_function("Emil", "Refsnes")

#----------------------------------------------------------------------------------------------------------------------

def my_function(*kids): # se o número de argumentos for desconhecido, adicione um * antes do nome do parametro 
  print("The youngest child is " + kids[2])

my_function("Emil", "Tobias", "Linus")

#-----------------------------------------------------------------------------------------------------------------------

def my_function(child3, child2, child1): #os argumento também poder ser através de chave = valor 
  print("The youngest child is " + child3)

my_function(child1 = "Emil", child2 = "Tobias", child3 = "Linus")

#----------------------------------------------------------------------------------------------------------------------

def my_function(**kid): #Se o argumento da palavra chave for desconhecido, adiciona o ** antes do nome
  print("His last name is " + kid["lname"])

my_function(fname = "Tobias", lname = "Refsnes")

#----------------------------------------------------------------------------------------------------------------------

def my_function(country = "Norway"): #Valor do parametro padrão, quando não foi especificado, utilizara o descrito 
  print("I am from " + country)

my_function("Sweden")
my_function("India")
my_function() #aqui no caso é Norway 
my_function("Brazil")

#----------------------------------------------------------------------------------------------------------------------

""" Você pode enviar qualquer tipo de dado de argumento para uma função (string, número, lista, dicionário etc.), e ele será tratado como o mesmo tipo de dado dentro da função.

Por exemplo, se você enviar uma Lista como argumento, ela ainda será uma Lista quando chegar à função: """

def my_function(food):
  for x in food:
    print(x)

fruits = ["apple", "banana", "cherry"]

my_function(fruits)

#-------------------------------------------------------------------------------------------------------------------------

#Função com retorno

def my_function(x):
  return 5 * x

print(my_function(3))
print(my_function(5))
print(my_function(9))

def somar (a, b): 
    resultado = a + b 
    return resultado
    
meu_resultado = somar (1, 2) 
print (meu_resultado) 

#--------------------------------------------------------------------------------------------------------------------------

#definições não podem estar vazias, mas se por algum motivo você tiver uma functiondefinição sem conteúdo, insira-a na passdeclaração para evitar um erro.
def myfunction():
  pass

#--------------------------------------------------------------------------------------------------------------------------

"""Você pode especificar que uma função pode ter SOMENTE argumentos posicionais ou SOMENTE argumentos de palavras-chave. """

def my_function(x, /): # Para especificar que uma função pode ter apenas argumentos posicionais, adicione , / após os argumentos:
  print(x)

my_function(3)

#Sem isso, , /você tem permissão para usar argumentos de palavras-chave, mesmo que a função espere argumentos posicionais:

def my_function(x):
  print(x)

my_function(x = 3)

#-----------------------------------------------------------------------------------------------------------------------------

def my_function(*, x): #Para especificar que uma função pode ter apenas argumentos de palavras-chave, adicione *, antes dos argumentos: (ao contrario do de cima)
  print(x)

my_function(x = 3)

""" Você pode combinar os dois tipos de argumentos na mesma função.

Qualquer argumento antes de / ,é somente posicional, e qualquer argumento depois de é *, somente palavra-chave. """

def my_function(a, b, /, *, c, d):
  print(a + b + c + d)

my_function(5, 6, c = 7, d = 8)

#--------------------------------------------------------------------------------------------------------------------------------

"""Python também aceita recursão de função, o que significa que uma função definida pode chamar a si mesma.

Recursão é um conceito matemático e de programação comum. Isso significa que uma função chama a si mesma. Isso tem o benefício de significar que você pode fazer um loop pelos dados para chegar a um resultado. """

def tri_recursion(k):
  if(k > 0):
    result = k + tri_recursion(k - 1)
    print(result)
  else:
    result = 0
  return result

print("Recursion Example Results:")
tri_recursion(6)

"""Neste exemplo, tri_recursion() é uma função que definimos para chamar a si mesma ("recurse"). 
Usamos a variável k como os dados, que decrementa ( -1 ) toda vez que recursionamos. 
A recursão termina quando a condição não é maior que 0 (ou seja, quando é 0)."""