# Atividade 5: Crie um dicionário com os dados de três pessoas contendo nome, idade e
# cidade. Use esse dicionário para criar um DataFrame.

import pandas as pd


pessoas = {
    "nomes": ["Ana Silva", "Bruno Costa", "Carla Santos", "Daniel Oliveira",
    "Eduarda Souza", "Felipe Lima", "Gabriela Rocha", "Henrique Alves",
    "Isabela Pereira", "João Mendes", "Karina Ferreira", "Lucas Gomes",
    "Mariana Torres", "Nicolas Barbosa", "Patrícia Martins"],
    "idades": [25, 32, 28, 19, 35, 22, 31, 27, 29, 24, 40, 18, 33, 45, 30],

    "cidades": ["São Paulo", "Rio de Janeiro", "Belo Horizonte", "Porto Alegre",
    "Salvador", "Recife", "Fortaleza", "Curitiba", "Manaus", "Brasília",
    "Florianópolis", "Vitória", "Natal", "Campo Grande", "João Pessoa"]
}

dfPessoas = pd.DataFrame(pessoas)

print(dfPessoas)