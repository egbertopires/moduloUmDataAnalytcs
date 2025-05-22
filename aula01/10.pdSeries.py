# Atividade 4: Crie uma Series com os números de 1 a 5 e defina índices
# personalizados em formato de letras

import pandas as pd

numeros = [1,2,3,4,5]

letras = ["a", "b", "c", "d", "e"]

serieNumeros = pd.Series(numeros,index=letras,dtype=int,name='primeiros cinco números')

print(serieNumeros)
