""" Conceito de Dicionários

- Um dicionário em Python é uma coleção de pares chave-valor. 
- Cada chave é única e é usada para acessar o valor correspondente. 
- Dicionários são mutáveis, o que significa que você pode alterar, adicionar ou remover itens após a criação.
- Um dicionário pode conter string simples, listas, ou até mesmos outros dicionários dentro de si. 

Estrutura de um Dicionário

- Um dicionário é definido usando chaves {} e os pares chave-valor são separados por dois pontos :. """

# Criando um dicionário
meu_dicio = {"nome": "Felipe", "idade": 25, "profissão": "Dev"}

# Acessar Valores: Você pode acessar o valor associado a uma chave usando colchetes [] ou o método .get().
# A diferença é que, se a chave não existir, [] retornará um erro, enquanto .get() retornará None.

print(meu_dicio ["idade"]) # print retorna 25
print (meu_dicio.get ('profissão')) # print retorna Dev

# alterar o valor da chave nome ou inclui uma nova chave: valor
meu_dicio ["nome"] = "Felipe Fernandes"

# Iterar Sobre Itens: Você pode iterar sobre as chaves e valores usando um loop for.
for chave, valor in meu_dicio.items():
    print(f"{chave}: {valor}") # Output: nome: Felipe Fernandes, idade: 25, profissão: Dev

# Adicionar ou Remover Itens: Você pode adicionar ou remover itens de um dicionário após a criação.
meu_dicio["cidade"] = "São Paulo"  # Adiciona um novo item
del meu_dicio["idade"]  # Remove um item

# Verificar se uma chave existe: Você pode verificar se uma chave existe em um dicionário usando o operador in.
print("nome" in meu_dicio)  # Output: True
print("idade" in meu_dicio)  # Output: False

# O método items() retorna uma lista de tuplas, onde cada tupla contém uma chave e seu valor correspondente.
print(meu_dicio.items())  # Output: dict_items([('nome', 'Felipe Fernandes'), ('profissão', 'Dev'), ('cidade', 'São Paulo')])

# Você pode usar o método keys() para obter uma lista de todas as chaves e values() para obter uma lista de todos os valores.
print(meu_dicio.keys())  # Output: dict_keys(['nome', 'profissão', 'cidade'])

# O método pop() remove um item com a chave especificada e retorna o valor correspondente.
valor = meu_dicio.pop("cidade")

# O método clear() remove todos os itens de um dicionário.
meu_dicio.clear()

# O método values() retorna uma lista de todos os valores no dicionário.
print(meu_dicio.values())  # Output: dict_values(['Felipe Fernandes', 'Dev', 'São Paulo'])

# Dicionários Aninhados: Você pode ter dicionários dentro de dicionários.
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

#Método get: O método get() é usado para acessar um valor de um dicionário, dado uma chave.
print (pessoa.get ('interesses')) # buscando alguma informação dentro do dicionário pessoa
print (pessoa.get ('interesses') [0]) # buscando uma informacão especifica dentro de uma lista 
print (pessoa.get ('pet').get ("nome")) #buscando uma informação especifica dentro de um dicionário

# vale lembrar, usar o get é o mesmo que usar as formulas abaixo.
print (pessoa ["interesses"])
print (pessoa ["interesses"] [0])
print (pessoa ["pet"]["nome"]) 

# Fromkeys: O método fromkeys() cria um novo dicionário com as chaves especificadas e o mesmo valor para todas as chaves.
dicionario = {}.fromkeys(["nome", "idade", "profissão"], "Desconhecido")
print(dicionario)  # Output: {'nome': 'Desconhecido', 'idade': 'Desconhecido', 'profissão': 'Desconhecido'}

# Update: O método update() atualiza um dicionário com outro dicionário ou com uma sequência de pares chave-valor.
dicionario.update({"nome": "Marcio", "idade": 35, "profissão": "Data Engineer"})
print(dicionario)  # Output: {'nome': 'Marcio', 'idade': 35, 'profissão': 'Data Engineer'}

# Copy: O método copy() cria uma cópia rasa de um dicionário.
copia = dicionario.copy()

# Setdefault: O método setdefault() retorna o valor da chave especificada se a chave existir. Caso contrário, ele insere a chave com o valor especificado e retorna o valor.
dicionario.setdefault("nome")  # Output: Marcio - por que a chave nome existe com o valor Marcio no dicionário
dicionario.setdefault("nome", "Roberto") # Output: Marcio - por que a chave nome existe com o valor Marcio no dicionário 
dicionario.setdefault("cor preferida", "verde")  # Output: verde

# Popitem: O método popitem() remove o último item inserido em um dicionário e retorna uma tupla contendo a chave e o valor removido.
item = dicionario.popitem()
print(item)  # Output: ('cor preferida', 'verde')

















