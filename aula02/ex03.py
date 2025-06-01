# 3. Mostre:
# O número de dimensões (ndim), forma (shape), tipo (dtype) e a quantidade de elementos (size) de um array 2D.
import numpy as np

# Criação de uma ndarray com números espaçados corretamente:

vetorMatriz = np.linspace(250,300)

# Transformando o vetorMatriz em uma matrizVetor:

matrizVetor = vetorMatriz.reshape(10,5)
print(f"Matriz com espaços iguais entre 250 e 300:\n\n"
      f"{matrizVetor}\n\n"
      f"Dimensões: {matrizVetor.ndim}\n"
      f"Tipo: {matrizVetor.dtype}\n"
      f"Quantidade de elementos: {matrizVetor.size}\n"
      f"Formato: {matrizVetor.shape}")

