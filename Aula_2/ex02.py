'''
Leia 10 números inteiros utilizando um array.
Determine:
- o maior valor;
- o menor valor;
- as posições em que eles aparecem.
'''

numeros = []

# Leitura dos 10 números
for i in range(10):
    numero = int(input(f"Digite o {i + 1}º número: "))
    numeros.append(numero)

# Encontrando o maior e o menor
maior = max(numeros)
menor = min(numeros)

# Exibindo os resultados
print("\nNúmeros digitados:", numeros)
print("\nMaior valor:", maior)

print("\nPosições do maior valor:")
for i in range(10):
    if numeros[i] == maior:
        print(i + 1, end=" ")

print("\nMenor valor:", menor)

print("\nPosições do menor valor:")
for i in range(10):
    if numeros[i] == menor:
        print(i + 1, end=" ")
