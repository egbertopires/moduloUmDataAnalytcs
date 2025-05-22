# Atividade 7: Crie um DataFrame a partir de uma lista de listas. Os dados devem
# representar [nome, idade] de três pessoas. Defina os nomes das colunas como "Nome" e
# "Idade".
import pandas as pd

celebridadesNordestinas = [
    [
        "Luiz Gonzaga", "Elba Ramalho", "Chico César", "Ivete Sangalo", "Alceu Valença",
        "Zé Ramalho", "Fagner", "Maria Bethânia", "Caetano Veloso", "Gal Costa",
        "Lenine", "Hermeto Pascoal", "Djavan", "Roberta Miranda",
        "Jackson do Pandeiro", "Dominguinhos", "Marinês", "Geraldo Azevedo",
        "Nando Cordel", "Silvério Pessoa"
    ],
    [
        76, 72, 60, 52, 78,
        74, 74, 77, 81, 77,
        65, 88, 75, 67,
        62, 72, 71, 79,
        70, 49
    ],
    [
        "Pernambuco", "Paraíba", "Paraíba", "Bahia", "Pernambuco",
        "Paraíba", "Ceará", "Bahia", "Bahia", "Bahia",
        "Pernambuco", "Alagoas", "Alagoas", "Paraíba",
        "Paraíba", "Pernambuco", "Pernambuco", "Pernambuco",
        "Pernambuco", "Pernambuco"
    ]
]

dfCelebridadesNordestinas = (
    pd.DataFrame(
    list(
        zip(*celebridadesNordestinas)
    ),
    columns=['nome','idade','naturalidade'])
)

print(dfCelebridadesNordestinas)


