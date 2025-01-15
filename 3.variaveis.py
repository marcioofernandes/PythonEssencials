camelCase = "Camel Case" #primeira letra minuscula, o restante maiuscula 
PascalCase = "Pascal Case" #Cada primeira letra maiuscula 
snake_case = "Snake Case" #palavras separadas por _ 

#maneiras permitidas de váriaveis 

myvar = "John"
my_var = "John"
_my_var = "John"
myVar = "John"
MYVAR = "John"
myvar2 = "John" 

# ------------------------------------------------------------------- 

# Atribuindo diversos valores em uma linha 

x, y, z = "Orange", "Banana", "Apple"

# Um valor para multiplas váriaveis 

x = y = z = "Orange"

# Transformando lista em váriaveis 

fruits = ["apple", "banana", "cherry"]
x, y, z = fruits 

# Variáveis de saída 

x = 'Python is awesome'
print (x) 

# or 

x = "Python"
y = "is"
z = "awesome"
print(x, y, z)

#or 

x = "Python "
y = "is "
z = "awesome"
print(x + y + z)

# Variaveis Globais

""" Se você criar uma variável com o mesmo nome dentro de uma função, 
essa variável será local, e só poderá ser usada dentro da função. 
A variável global com o mesmo nome permanecerá como era, global e com o valor original."""

x = "awesome"

def myfunc():
  x = "fantastic"
  print("Python is " + x)

myfunc()

print("Python is " + x)

# Palavra chave "Global"

def myfunc():
  global x # Se você usar a globalpalavra-chave, a variável pertence ao escopo global:
  x = "fantastic"

myfunc()

print("Python is " + x)

# alterando a palavra chave dentro da função 

x = "awesome"

def myfunc():
  global x # Para alterar o valor de uma variável global dentro de uma função, consulte a variável usando a globalpalavra-chave:
  x = "fantastic"

myfunc()

print("Python is " + x)

