import pandas as pd

# 1. Criando uma Series a partir de uma lista

listaPdSerie = [1,2,3]
serieNotas = pd.Series(listaPdSerie)

# 2. Definindo um índice personalizado

indice = ['A','B','C']
serieNotas = pd.Series(listaPdSerie,indice)

# 3. Criando a partir de uma lista com dicionários

# dados = [
#     {"nome": "Ana", "idade": 23},
#     {"nome": "Bruno", "idade": 25},
#     {"nome": "Carlos", "idade": 30},
#     {"nome": "Diana", "idade": 20}
# ]
#
# serieDados = pd.Series(dados)
#
# print(serieDados)


# 4. Criando a partir de um valor escalar(repetido)

serieNotas = pd.Series(5,indice)

# 5. Usando o parâmetro dtype e name
listaNova = [1.5,1.3,0.5]

serieNotas = pd.Series(listaNova,dtype=float,name='aprender')

print(serieNotas)