



def generate_report(main_tank, external_tank, hydrogen_tank): # Definiu a função, onde o nome é "generate report", e ela possui 3 parametros "main_...", quando a função for chamada, vai atribuir os numeros indicados aos respectivos parametros. 
    average_fuel = (main_tank + external_tank + hydrogen_tank) / 3 # aqui é uma váriavel criada para armazenar o valor do cálculo, que faz a soma dos 3 valores e divide por 3 
    report = f""" 
    Relatório de Combustível:
    -------------------------
    Tanque Principal: {main_tank} litros
    Tanque Externo: {external_tank} litros
    Tanque de Hidrogênio: {hydrogen_tank} litros
    Média de Combustível: {average_fuel:.2f} litros
    """ #report = cria uma váriavel que vai apresentar o relatório em format fstring - o f""" indica que uma string será formatada e permite incluir variaveis dentro de {}
    return report # retorna a função, ou seja, ela retorna a string formatada "report" gerada anteriormente com os valores apreseentados 


print(generate_report (80,70,75))

