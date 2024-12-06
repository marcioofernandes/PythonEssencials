texto = "Aula PycodeBR" #Cada caractere é indicado por um número começando com o Zero
print(texto [5:11]) #nesse caso o caractere 11 não é incluído 
print (texto [5:]) # se você não declarar o final, ele percorre o texto completo, o mesmo para o ínicio
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