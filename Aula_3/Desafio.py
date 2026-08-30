# Classe Paciente
class Paciente:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        self.prioridade = idade >= 60
    def __str__(self):
        if self.prioridade:
            return f"{self.nome} - {self.idade} anos - PRIORIDADE"
        else:
            return f"{self.nome} - {self.idade} anos - Normal"

# Classe Node
class Node:
    def __init__(self, paciente):
        self.dado = paciente
        self.proximo = None

# Classe FilaClinica
class FilaClinica:
    def __init__(self):
        self.inicio = None
        self.fim = None
        self._tamanho = 0

    # Verifica se a fila está vazia
    def esta_vazia(self):
        return self.inicio is None

    # Retorna o tamanho da fila
    def tamanho(self):
        return self._tamanho

    # Adiciona um paciente na fila
    def adicionar(self, paciente):
        novo = Node(paciente)

        # Se a fila estiver vazia
        if self.esta_vazia():
            self.inicio = novo
            self.fim = novo

        # Se o paciente tiver prioridade
        elif paciente.prioridade:
            # Procura o último paciente prioritário
            atual = self.inicio
            anterior = None
            while atual is not None and atual.dado.prioridade:
                anterior = atual
                atual = atual.proximo

            # Se todos os pacientes anteriores forem prioritários
            if anterior is not None:
                novo.proximo = atual
                anterior.proximo = novo
            else:
                # Insere no início
                novo.proximo = self.inicio
                self.inicio = novo

        # Paciente normal entra no final
        else:
            self.fim.proximo = novo
            self.fim = novo
        self._tamanho += 1

    # Atende o primeiro paciente da fila
    def atender(self):
        if self.esta_vazia():
            print("Não há pacientes para atender.")
            return None
        paciente = self.inicio.dado
        self.inicio = self.inicio.proximo

        # Se a fila ficou vazia
        if self.inicio is None:
            self.fim = None
        self._tamanho -= 1
        print(f"Atendendo: {paciente.nome}")
        return paciente
 
    # Lista todos os pacientes
    def listar(self):
        if self.esta_vazia():
            print("A fila está vazia.")
            return
        atual = self.inicio
        print("\n--- FILA DA CLÍNICA ---")
        while atual is not None:
            print(atual.dado)
            atual = atual.proximo
        print("-----------------------")


# TESTANDO O PROGRAMA

fila = FilaClinica()

# Cinco pacientes
p1 = Paciente("Ana", 25)
p2 = Paciente("Carlos", 65)
p3 = Paciente("Maria", 40)
p4 = Paciente("João", 70)
p5 = Paciente("Pedro", 30)

# Adicionando os pacientes
fila.adicionar(p1)
fila.adicionar(p2)
fila.adicionar(p3)
fila.adicionar(p4)
fila.adicionar(p5)

# Listando a fila
fila.listar()

# Mostrando o tamanho
print("\nTamanho da fila:", fila.tamanho())

# Atendendo pacientes
print("\n--- ATENDIMENTO ---")
fila.atender()
fila.atender()

# Listando novamente
fila.listar()

# Verificando se está vazia
print("\nA fila está vazia?", fila.esta_vazia())
print("\nTamanho atual:", fila.tamanho())
