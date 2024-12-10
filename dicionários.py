""" No dicionário o que difere de lista, é que você possui "chave" e "valor """

# Lista 

lista = ["um", "dois", "três"]
lista [0] # retorna "um"

# Dicionário 

meu_dicio = {"nome": "Felipe", "idade": 25, "profissão": "Dev"} #dicionários são atribuidos atraves do {}

meu_dicio ["idade"] # print retorna 25
meu_dicio ["nome"] # print retorna Felipe 
meu_dicio ["profissão"] # print retorna Dev 

print (meu_dicio.get ('profissão')) # Outra forma de pesquisar dentro do dicionário 

for chave, valor in meu_dicio.items(): # comando para mostrar os itens dentro do dicionário 
    print (f"{chave}: {valor}") 

# meu_dicio.pop ("idade") # remove a chave idade do dicionário
print (meu_dicio.keys ()) # mostra as chaves contidas no dicionário 
print (meu_dicio.values ()) # mostra os valores contidos no dicionário 
meu_dicio. clear () # Limpa todos os valores dentro do dicionário 

"""-------------------------------------------------------------------------------"""

# Um dicionário pode conter string simples, listas, ou até mesmos outros dicionários dentro de si. 

pessoa = {
    "nome": "Marcio",
    "idade": 35,
    "profissão": "Engenheiro de dados",
    "interesses" :["Python", "Programação", "SQL"], 
    "pet": {
        "nome": "Duque",
        "idade": 3, 
        "peso": "29kg",
    }
}

print (pessoa.get ('interesses')) # buscando alguma informação dentro do dicionário pessoa 
print (pessoa.get ('interesses') [0]) # buscando uma informacão especifica dentro de uma lista 
print (pessoa.get ('pet').get ("nome")) #buscando uma informação especifica dentro de um dicionário

# vale lembrar, usar o get é o mesmo que usar as formulas abaixo 

print (pessoa ["interesses"])
print (pessoa ["interesses"] [0])
print (pessoa ["pet"]["nome"]) 

"""--------------------------------------------------------------------------------------------"""

pessoa["ano_nascimento"] = 1989 # adiciona uma nova chave: valor dentro do dicionário 
pessoa ['cores_favoritas'] = ['Verde', "Branco", "Cinza", "Marrom"]
pessoa ["mãe"] = {
    "nome": "Lucilene",
    "idade": 50
}

for chave, valor in pessoa.items(): # comando para mostrar os itens dentro do dicionário 
    print (f"{chave}: {valor}") 

