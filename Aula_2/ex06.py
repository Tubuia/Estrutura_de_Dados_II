'''
Leia uma matriz 4 x 4.
Mostre os elementos da diagonal principal e calcule sua soma.
'''

# Cria a matriz
matriz = []

# Lê os valores da matriz
for i in range(4):
    linha = []
    for j in range(4):
        numero = int(input(f"Digite o valor [{i}][{j}]: "))
        linha.append(numero)
    matriz.append(linha)

# Exibe a matriz
print("\nMatriz:")
for linha in matriz:
    print(linha)

# Mostra a diagonal principal e calcula sua soma
soma = 0

print("\nDiagonal principal:")

for i in range(4):
    print(matriz[i][i], end=" ")
    soma += matriz[i][i]

# Mostra a soma da diagonal principal
print("\nSoma da diagonal principal:", soma)


