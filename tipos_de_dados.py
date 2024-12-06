"""
            TIPO DE DADOS 

str = tipo de texto 
int, float, complex = tipos numéricos 
list, tuple, range = tipos de sequencia 
dict = tipo de mapeamento 
set, frozenset = tipos de conjuntos 
bool = tipo boleano 
bytes, bytearray, memoryview = tipos binários 
NoneType = nenhum tipo 

"""

x = str ("Hello World")
x = int (20)
x = float (20.5)
x = complex (1j)
x = list (("apple", "Banana"))
x = tuple(("apple", "banana", "cherry"))
x = range (6) 
x = dict (name = "John", age=36)
x = set(("apple", "banana", "cherry"))
x = frozenset(("apple", "banana", "cherry"))
x = bool(5)
x = bytes(5)
x = bytearray(5)
x = memoryview(bytes(5))

#Convertendo tipos númericos 

x = 1    # int
y = 2.8  # float
z = 1j   # complex

#convert from int to float:
a = float(x)

#convert from float to int:
b = int(y)

#convert from int to complex:
c = complex(x)

print(a)
print(b)
print(c)

print(type(a))
print(type(b))
print(type(c))

# Criando número aleatório no Python 

import random

print(random.randrange(1, 10))