import numpy as np

# 2. Faça:
# 	A soma de dois arrays.
# 	A multiplicação de um array por um número.
# 	O quadrado de todos os elementos de um array.


# Criando duas matrizes de números inteiros
# matriz um sem números aleátorios
# matriz dois com números aleátorios

vetorUm = np.arange(1,20+1)
matrizUm = vetorUm.reshape(5,4)

matrizDois = np.random.randint(low=150,high=(170 + 1),size=(5,4))
print(matrizUm)
print(matrizDois)

somarArray = matrizUm + matrizDois
print(somarArray)

multiplicarArray = matrizUm * 150
print(multiplicarArray)

elevarArray = matrizDois ** 2
print(elevarArray)