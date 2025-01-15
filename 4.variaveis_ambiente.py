''' Variáveis de ambientes nada mais são do que variaveis que você salva/configura 
no sistema operacional, ou seja, no ambiente em que sua aplicação irá rodar. '''

import api_fake # importou a api_fake que criou para rodar o exercicio

""" AQUI VOCË CRIOU AS VARIAVEIS DE AMBIENTE ATRAVÉS DO TERMINAL
export NOME_VARIAVEL=valor_variavel
(consulta) echo $NOME_VARIAVEL 
"""

import os # importar sistema operacional no código 

usuario = os.environ.get("USUARIO_API") #código para buscar no sistema operacional as variáveis salvas 
senha = os.environ.get("SENHA_API")
ambiente = os.environ.get("AMBIENTE")

login = api_fake.login (usuario, senha) 
print (login)

if ambiente == "dev": 
    print (api_fake.envia_email_log())