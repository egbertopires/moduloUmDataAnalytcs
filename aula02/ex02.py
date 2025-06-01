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
print(f'Matriz com números sequenciais inteiros:\n'
      f'{matrizUm}\n')

print(f'Matriz com números aleatórios inteiros:\n'
      f'{matrizDois}\n')

somarArray = matrizUm + matrizDois
print(f'Soma das matrizes anteriores:\n'
      f'{somarArray}\n')

multiplicarArray = matrizUm * 150
print(f'Somando a matriz um pelo escalar 150:\n'
      f'{multiplicarArray}\n')

elevarArray = matrizUm ** 2
print(f'Quadrado da matriz um:\n'
      f'{elevarArray}\n')