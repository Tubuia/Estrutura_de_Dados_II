'''
Crie uma struct Produto contendo:
- nome
- codigo
- preco
- quantidade
- Cadastre cinco produtos.
Depois:
- mostre todos os produtos;
- calcule o valor total de cada produto;
- informe o produto com maior valor em estoque.
'''

# Lista para armazenar os 5 produtos
produtos = []

# Cadastro dos 5 produtos
for i in range(5):
    print(f"\nProduto {i + 1}")
    produto = {
        "nome": input("Nome: "),
        "codigo": int(input("Código: ")),
        "preco": float(input("Preço: ")),
        "quantidade": int(input("Quantidade: "))
    }
    produtos.append(produto)

# Mostra todos os produtos
print("\nPRODUTOS CADASTRADOS")
for produto in produtos:
    valor_total = produto["preco"] * produto["quantidade"]
    print(f"\nNome: {produto['nome']}")
    print(f"Código: {produto['codigo']}")
    print(f"Preço: R$ {produto['preco']:.2f}")
    print(f"Quantidade: {produto['quantidade']}")
    print(f"Valor em estoque: R$ {valor_total:.2f}")

# Encontra o produto com maior valor em estoque
maior = produtos[0]
for produto in produtos:
    valor_atual = produto["preco"] * produto["quantidade"]
    valor_maior = maior["preco"] * maior["quantidade"]
    if valor_atual > valor_maior:
        maior = produto

# Mostra o produto com maior valor em estoque
valor_maior = maior["preco"] * maior["quantidade"]

print("\nMAIOR VALOR EM ESTOQUE")
print(f"Nome: {maior['nome']}")
print(f"Código: {maior['codigo']}")
print(f"Valor em estoque: R$ {valor_maior:.2f}")

