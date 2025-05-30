import numpy as np

# 1. Crie:
# 	Um array 1D de 5 inteiros.
# 	Uma matriz 3x3 de números aleatórios inteiros entre 0 e 10.


vetor = np.arange(1,5+1)
print(vetor)
print('\n')

# np.random.randint(início, fim, size) - números aleátorios inteiros
matrizAleatorioInt = np.random.randint(0,11,size=(3,3) )
print(matrizAleatorioInt)
print('\n')


# np.random.rand(shape) - números aleátorios entre 0 e 1 do tipo foalt
# são separados de forma igual
matrizAleatoriofloat = np.random.rand(3,3)
print(matrizAleatoriofloat)