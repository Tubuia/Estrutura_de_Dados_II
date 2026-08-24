'''
Uma turma possui 4 alunos e 3 avaliações.
Crie uma matriz para armazenar as notas.
Calcule e apresente a média de cada aluno.
'''

# Cria a matriz para armazenar as notas dos 4 alunos
# Cada aluno terá 3 notas
notas = []

# Lê as notas dos 4 alunos
for i in range(4):
    aluno = []
    for j in range(3):
        nota = float(input(f"Digite a nota {j + 1} do aluno {i + 1}: "))
        aluno.append(nota)
    notas.append(aluno)

# Exibe a matriz de notas
print("\nNotas dos alunos:")
for aluno in notas:
    print(aluno)

# Calcula e apresenta a média de cada aluno
print("\nMédia de cada aluno:")

for i in range(4):
    media = sum(notas[i]) / 3
    print(f"Aluno {i + 1}: {media:.2f}")
