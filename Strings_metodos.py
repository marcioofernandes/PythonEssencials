texto = "Aula PycodeBR" #Cada caractere é indicado por um número começando com o Zero
#Você pode retornar um intervalo de caracteres usando a sintaxe de fatia
#Especifique o índice inicial e o índice final, separados por dois pontos, para retornar uma parte da string.
print(texto [5:11]) #nesse caso o caractere 11 não é incluído 
print (texto [5:]) # se você não declarar o final, ele percorre o texto completo, o mesmo para o ínicio
#Use índices negativos para iniciar a fatia a partir do final da string:
b = "Hello, World!"
print(b[-5:-2])
print (len(texto)) # trás o tamanho (em caractere) do texto 
print (texto.count("a")) # conta quantos caracteres declarados contém no texto, serve se quiser colocar a palavra tbm
print (texto.count("a",5,11)) # conta quantos caracteres informados contém no texto, declarando de onde começar e onde terminar 
print (texto.find ("Aula")) # procure em qual posição está o objeto declarado 
print (texto.upper()) # deixa o texto todo maiusculo / .lower (deixa em minusculo)
print (texto.capitalize()) # deixa a primeira letra maiscula e o resto minusculo 
print (texto.title()) #deixa cada letra da palavra maiscula e o restante minuscula 
print (texto.split()) # retorna uma lista de todas as palavras contidas no seu texto 
lista_de_palavras = texto.split() 
print ("_".join(lista_de_palavras)) #junta a lista de palavra declarada, se não declarar nenhum separador, ele cola tudo
print (texto.strip()) #limpa os espaços do começo e no final 
print (texto.rstrip()) # limpa os espaços da direita / se usar o lstrip remove da esquerda 
a = "Hello, World!"
print(a.replace("H", "J")) # O replace()método substitui uma string por outra string:
"""-------------------------------------------------------------------------------------"""
# F-STRINGS

'''Para especificar uma string como uma f-string, basta colocar um f na frente do literal da string e 
adicionar chaves {}como espaços reservados para variáveis ​​e outras operações.'''

age = 36
txt = f"My name is John, I am {age}"
print(txt)

#modificadores

'''Um modificador é incluído adicionando dois pontos :seguidos de um tipo 
de formatação legal, como .2f o que significa número de ponto fixo com 2 decimais:'''

price = 59
txt = f"The price is {price:.2f} dollars"
print(txt)

#Um espaço reservado pode conter código Python, como operações matemáticas:

txt = f"The price is {20 * 59} dollars"
print(txt)

"""----------------------------------------------------------------------------------"""

# Strings multilinhas 

a = """Olá, meu nome é Marcio. 
E é assim que você atribui umas string multilinhas
para quando fizer o print, aparecer o texto dessa forma. 
Lembre-se, se quiser adicionar alguma variável aqui dentro, 
basta colocar o f na frente. """

print (a)

"""------------------------------------------------------------------------"""
# looping através de uma string 

for x in "banana": # faz o looping pelas letras da palavra "banana"
  print(x) 

"""--------------------------------------------------------------------------"""
#Verificar sequência de caracteres

txt = "The best things in life are free!"
print("free" in txt) #verifica se a palavra digitada está contida no texto, retorna True ou False

# use o if se quiser uma declaração 
txt = "The best things in life are free!"
if "free" in txt:
  print("Yes, 'free' is present.")

# Para verificar se uma determinada frase ou caractere NÃO está presente em uma string, podemos usar a palavra-chave not in.

txt = "The best things in life are free!"
print("expensive" not in txt)

#Use-o em uma if declaração:

txt = "The best things in life are free!"
if "expensive" not in txt:
  print("No, 'expensive' is NOT present.")

"""------------------------------------------------------------------------------"""

# caracteres de escape 

'''Caracteres de escape permitem representar caracteres ou comportamentos especiais em strings.
Eles são úteis para formatar texto, lidar com aspas ou inserir caracteres invisíveis como quebras de linha ou tabulações.
Se você quiser evitar caracteres de escape, use strings cruas (r"").
'''

txt = "We are the so-called \"Vikings\" from the north."
print (txt)

txt = 'It\'s alright.' #aspas simples
print(txt) 

txt = "This will insert one \\ (backslash)." #backslash 
print(txt) 

txt = "Hello\nWorld!" # nova linha 
print(txt) 

txt = "Ola\rMundo!" # Retorno de carro (aparentemente só mostra o que vem depois do R)
print(txt) 

txt = "Hello\tWorld!" #tab entre as palavras
print(txt) 

#Este exemplo irá apagar o (backspace) do texto
txt = "Hello \bWorld!"
print(txt) 

txt = "Linha 1\fLinha 2"
print(txt) 

txt = "\110\145\154\154\157" ##Uma barra invertida seguida de três números inteiros resultará em um valor octal:
print(txt) 

#Uma barra invertida seguida por um 'x' e um número hexadecimal representa um valor hexadecimal:

txt = "\x48\x65\x6c\x6c\x6f"
print(txt) 
