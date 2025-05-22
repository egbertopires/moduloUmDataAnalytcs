# Atividade 3: Crie uma Series usando um dicionário onde as chaves são nomes
# de alunos e os valores são suas notas finais.

import pandas as pd

notas_finais = {
    "Ana": 8.5,
    "Bruno": 7.2,
    "Carla": 9.0,
    "Daniel": 6.8,
    "Eduarda": 7.5,
    "Felipe": 8.0,
    "Gustavo": 5.9,
    "Helena": 9.3,
    "Igor": 6.5,
    "Juliana": 8.7
}

serieNotaFinal = pd.Series(notas_finais)

print(serieNotaFinal)