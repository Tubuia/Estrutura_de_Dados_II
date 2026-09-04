from collections import deque


class FilaAtendimento:
    def __init__(self):
        # Cria a fila de pacientes
        self.fila = deque()

    def adicionar_paciente(self, nome, prioritario=False):
        if prioritario:
            # Paciente prioritário entra no início da fila
            self.fila.appendleft(nome)
            print(f"Paciente prioritário '{nome}' entrou no início da fila.")
        else:
            # Paciente normal entra no final da fila
            self.fila.append(nome)
            print(f"Paciente normal '{nome}' entrou no final da fila.")

    def atender_paciente(self):
        if not self.fila:
            print("Não há pacientes aguardando atendimento.")
            return
        # Remove o primeiro paciente da fila
        paciente = self.fila.popleft()
        print(f"Atendendo paciente: {paciente}")

    def mostrar_fila(self):
        if not self.fila:
            print("A fila está vazia.")
            return
        print("\nFila de atendimento:")
        for posicao, paciente in enumerate(self.fila, start=1):
            print(f"{posicao}º - {paciente}")


# Exemplo de utilização

fila = FilaAtendimento()

# Pacientes normais entram no final
fila.adicionar_paciente("João")
fila.adicionar_paciente("Maria")
fila.adicionar_paciente("Carlos")

fila.mostrar_fila()

# Paciente prioritário entra no início
fila.adicionar_paciente("Dona Ana - Idosa", prioritario=True)

fila.mostrar_fila()

# Outro paciente prioritário
fila.adicionar_paciente("Pedro - Emergência", prioritario=True)

fila.mostrar_fila()

# Atendimento segue a prioridade
fila.atender_paciente()
fila.atender_paciente()
fila.atender_paciente()
fila.atender_paciente()
