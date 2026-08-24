'''
Leia 10 números e armazene-os em um array.
Mostre o vetor original e o vetor invertido.
'''

# Cria o array e armazena os 10 números
numeros = []

for i in range(10):
    numero = int(input(f"Digite o {i + 1}º número: "))
    numeros.append(numero)

# Inverte o array
invertido = numeros[::-1]

# Mostra o vetor original e o vetor invertido
print("\nVetor original:", numeros)
print("\nVetor invertido:", invertido)

