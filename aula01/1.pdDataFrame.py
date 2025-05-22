import pandas as pd


# 1. Criando um DataFrame a partir de um dicionário de listas

dadosLista = {
    "nomes":['Ana','João','Maria'],
    "idade":[23,35,31],
    "notas":[8.5, 7, 9.2]
}

dfDadosLista = pd.DataFrame(dadosLista)
print(dfDadosLista)
print('')

# 2. Definindo um índice personalizado

indices = ['A','B','C']

dfDadosLista2 = pd.DataFrame(dadosLista,index=indices)
print(dfDadosLista2)
print('')
# 3. Criando a partir de uma lista de dicionários

listaDicionario = [
    {"nome":"Ana", "idade": 23, "nota":10},
    {"nome":"João", "idade": 35, "nota":8},
    {"nome":"Pedro", "idade": 23, "nota":6},
]

dfListaDicionario = pd.DataFrame(listaDicionario)
print(dfListaDicionario)
print('')
