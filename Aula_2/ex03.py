'''
Leia 20 números inteiros e armazene-os em um array.
Depois:
- mostre somente os números pares;
- conte quantos números pares existem;
- calcule a soma dos números pares.
'''

# Cria o array e armazena os 20 números
numeros = []

for i in range(20):
    numero = int(input(f"Digite o {i + 1}º número: "))
    numeros.append(numero)

# Variáveis para contar e somar os números pares
quantidade_pares = 0
soma_pares = 0

# Percorre o array e verifica os números pares
for numero in numeros:
    if numero % 2 == 0:
        print(numero, end=" ")
        quantidade_pares += 1
        soma_pares += numero

# Exibe a quantidade e a soma dos números pares
print("\nQuantidade de números pares:", quantidade_pares)
print("\nSoma dos números pares:", soma_pares)
