'''
Crie uma matriz 3 x 3 de números inteiros.

O programa deverá:
- ler os valores;
- mostrar a matriz;
- calcular a soma de todos os elementos;
- mostrar o maior valor.
'''

# Cria a matriz
matriz = []

# Lê os valores da matriz
for i in range(3):
    linha = []
    for j in range(3):
        numero = int(input(f"Digite o valor [{i}][{j}]: "))
        linha.append(numero)
    matriz.append(linha)

# Mostra a matriz
print("\nMatriz:")
for linha in matriz:
    print(linha)

# Calcula a soma e encontra o maior valor
soma = 0
maior = matriz[0][0]

for i in range(3):
    for j in range(3):
        soma += matriz[i][j]

        if matriz[i][j] > maior:
            maior = matriz[i][j]

# Mostra os resultados
print("\nSoma dos elementos:", soma)
print("Maior valor:", maior)

