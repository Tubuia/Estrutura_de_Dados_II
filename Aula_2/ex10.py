'''
Crie um pequeno sistema para cadastro de 10 funcionários.
Utilize um dicionario contendo:
- nome
- idade
- cargo
- salario
O programa deverá permitir:
- Cadastrar os funcionários.
- Listar todos os funcionários.
- Mostrar o funcionário com maior salário.
- Calcular a média salarial.
- Mostrar os funcionários com salário acima da média.
'''
# Lista para armazenar os funcionários
funcionarios = []

# Menu principal
while True:
    print("="*30)
    print("   SISTEMA DE FUNCIONÁRIOS   ")
    print("="*30)
    print("\n1 - Cadastrar funcionários")
    print("2 - Listar funcionários")
    print("3 - Mostrar funcionário com maior salário")
    print("4 - Calcular média salarial")
    print("5 - Mostrar funcionários acima da média")
    print("0 - Sair")
    opcao = int(input("\nEscolha uma opção: "))

    # Cadastra 10 funcionários
    if opcao == 1:
        funcionarios.clear()
        for i in range(10):
            print(f"\nFuncionário {i + 1}")
            funcionario = {
                "nome": input("Nome: "),
                "idade": int(input("Idade: ")),
                "cargo": input("Cargo: "),
                "salario": float(input("Salário: R$ "))
            }
            funcionarios.append(funcionario)
        print("\nFuncionários cadastrados com sucesso!")

    # Lista todos os funcionários
    elif opcao == 2:
        if len(funcionarios) == 0:
            print("\nNenhum funcionário cadastrado.")
        else:
            print("\n===== FUNCIONÁRIOS =====")
            for funcionario in funcionarios:
                print(f"\nNome: {funcionario['nome']}")
                print(f"Idade: {funcionario['idade']}")
                print(f"Cargo: {funcionario['cargo']}")
                print(f"Salário: R$ {funcionario['salario']:.2f}")

    # Mostra o funcionário com maior salário
    elif opcao == 3:
        if len(funcionarios) == 0:
            print("\nNenhum funcionário cadastrado.")
        else:
            maior = funcionarios[0]
            for funcionario in funcionarios:
                if funcionario["salario"] > maior["salario"]:
                    maior = funcionario
            print("\n===== MAIOR SALÁRIO =====")
            print(f"Nome: {maior['nome']}")
            print(f"Cargo: {maior['cargo']}")
            print(f"Salário: R$ {maior['salario']:.2f}")

    # Calcula a média salarial
    elif opcao == 4:
        if len(funcionarios) == 0:
            print("\nNenhum funcionário cadastrado.")
        else:
            soma = 0
            for funcionario in funcionarios:
                soma += funcionario["salario"]
            media = soma / len(funcionarios)
            print(f"\nMédia salarial: R$ {media:.2f}")

    # Mostra funcionários com salário acima da média
    elif opcao == 5:
        if len(funcionarios) == 0:
            print("\nNenhum funcionário cadastrado.")
        else:
            soma = 0
            for funcionario in funcionarios:
                soma += funcionario["salario"]
            media = soma / len(funcionarios)
            print(f"\n===== ACIMA DA MÉDIA (R$ {media:.2f}) =====")
            for funcionario in funcionarios:
                if funcionario["salario"] > media:
                    print(
                        f"{funcionario['nome']} - "
                        f"R$ {funcionario['salario']:.2f}"
                    )

    # Encerra o programa
    elif opcao == 0:
        print("\nPrograma encerrado.")
        break
    else:
        print("\nOpção inválida!")
