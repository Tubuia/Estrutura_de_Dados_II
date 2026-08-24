'''
Crie um programa que leia 10 números inteiros e armazene-os em um array.
Ao final, apresente:
- todos os números;
- a soma dos elementos;
- a média dos valores.
'''

numeros = []
soma = 0

# Leitura dos 10 números
for i in range(10):
    numero = int(input(f"Digite o {i + 1}º número inteiro: "))
    numeros.append(numero)
    soma += numero

# Cálculo da média
media = soma / 10

# Exibição dos resultados
print("\nNúmeros digitados:")
for numero in numeros:
    print(numero, end=" ")

print(f"\nSoma dos elementos: {soma}")
print(f"\nMédia dos valores: {media:.2f}")
