# Atividade 1: Crie uma lista com os nomes de cinco frutas e transforme essa lista
# em uma Series do pandas.
import pandas as pd

frutas = ["maçã", "banana", "laranja", "uva", "abacaxi"]

serieFrutas = pd.Series(frutas,name='nome das frutas')

print(serieFrutas)