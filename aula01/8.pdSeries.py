# Atividade 2: Crie uma lista com os valores de temperatura ao longo de 7 dias.
# Crie uma Series que use os dias da semana como índice.

import pandas as pd

dias = ["segunda", "terça", "quarta", "quinta", "sexta", "sábado", "domingo"]

temperaturas = [22.5, 23.0, 21.8, 24.1, 22.9, 20.3, 23.7]

serieTemperaturas = pd.Series(temperaturas,index=dias, name='temperaturas da primeira semana de maio 2025')

print(serieTemperaturas)