import pandas as pd

# Atividade 6: Crie uma lista de dicionários representando três livros, com as chaves: "título",
# "autor", "ano". Use essa lista para criar um DataFrame.

livrosClassicos = {
    "título": [
        "Dom Casmurro", "Memórias Póstumas de Brás Cubas", "O Cortiço", "Iracema", "Senhora",
        "Vidas Secas", "Capitães da Areia", "A Moreninha", "O Guarani", "Triste Fim de Policarpo Quaresma",
        "São Bernardo", "Lucíola", "Inocência", "Macunaíma", "A Escrava Isaura",
        "O Ateneu", "Marília de Dirceu", "Clara dos Anjos", "Os Sertões", "Canaã"
    ],
    "autor": [
        "Machado de Assis", "Machado de Assis", "Aluísio Azevedo", "José de Alencar", "José de Alencar",
        "Graciliano Ramos", "Jorge Amado", "Joaquim Manuel de Macedo", "José de Alencar", "Lima Barreto",
        "Graciliano Ramos", "José de Alencar", "Visconde de Taunay", "Mário de Andrade", "Bernardo Guimarães",
        "Raul Pompeia", "Tomás Antônio Gonzaga", "Lima Barreto", "Euclides da Cunha", "Graça Aranha"
    ],
    "ano": [
        1899, 1881, 1890, 1865, 1875,
        1938, 1937, 1844, 1857, 1915,
        1934, 1862, 1872, 1928, 1875,
        1888, 1792, 1948, 1902, 1902
    ]
}

dfLivrosClassicos = pd.DataFrame(livrosClassicos)

print(dfLivrosClassicos)

