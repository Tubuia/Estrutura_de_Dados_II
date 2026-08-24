'''
Crie um dicionatio Aluno contendo:
- nome
- idade
- nota1
- nota2
- nota3
Cadastre cinco alunos.
Calcule a média de cada aluno e classifique:
- Média >= 7,0 → Aprovado
- Média < 7,0  → Reprovado
Ao final, informe:
- quantidade de aprovados;
- quantidade de reprovados;
- aluno com maior média.
'''

# Lista para armazenar os 5 alunos
alunos = []

# Cadastro dos 5 alunos
for i in range(5):
    print(f"Aluno {i + 1}")
    aluno = {
        "nome": input("Nome: "),
        "idade": int(input("Idade: ")),
        "nota1": float(input("Nota 1: ")),
        "nota2": float(input("Nota 2: ")),
        "nota3": float(input("Nota 3: "))
    }
    alunos.append(aluno)

# Variáveis para contar aprovados e reprovados
aprovados = 0
reprovados = 0

# Inicializa o aluno com maior média
maior_media = alunos[0]
media_maior = (
    alunos[0]["nota1"] +
    alunos[0]["nota2"] +
    alunos[0]["nota3"]
) / 3

# Calcula a média e classifica cada aluno
print("\nRESULTADO DOS ALUNOS")
for aluno in alunos:
    media = (
        aluno["nota1"] +
        aluno["nota2"] +
        aluno["nota3"]
    ) / 3
    if media >= 7:
        situacao = "Aprovado"
        aprovados += 1
    else:
        situacao = "Reprovado"
        reprovados += 1
    print(f"\nNome: {aluno['nome']}")
    print(f"Idade: {aluno['idade']}")
    print(f"Média: {media:.2f}")
    print(f"Situação: {situacao}")

    # Verifica se este aluno possui a maior média
    if media > media_maior:
        media_maior = media
        maior_media = aluno

# Exibe o resultado final
print("\nRESULTADO FINAL")
print(f"Quantidade de aprovados: {aprovados}")
print(f"Quantidade de reprovados: {reprovados}")
print(f"Aluno com maior média: {maior_media['nome']}")
print(f"Maior média: {media_maior:.2f}")
