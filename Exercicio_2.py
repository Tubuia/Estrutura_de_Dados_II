from collections import deque


class SpoolerImpressora:
    def __init__(self):
        # Cria a fila de documentos
        self.fila = deque()

    def adicionar_documento(self, documento):
        # Adiciona o documento ao final da fila
        self.fila.append(documento)
        print(f"Documento '{documento}' foi adicionado à fila.")

    def imprimir_documento(self):
        # Verifica se existem documentos na fila
        if not self.fila:
            print("Não há documentos para imprimir.")
            return
        # Remove o documento mais antigo da fila
        documento = self.fila.popleft()
        print(f"Imprimindo documento: '{documento}'")

    def mostrar_fila(self):
        if not self.fila:
            print("A fila está vazia.")
            return
        print("\nDocumentos aguardando impressão:")
        for documento in self.fila:
            print(f"- {documento}")



# Exemplo de utilização

spooler = SpoolerImpressora()

# Documentos são adicionados à fila
spooler.adicionar_documento("Trabalho.pdf")
spooler.adicionar_documento("Relatorio.docx")
spooler.adicionar_documento("Curriculo.pdf")

spooler.mostrar_fila()

# A impressão segue a ordem de chegada
spooler.imprimir_documento()
spooler.imprimir_documento()

spooler.mostrar_fila()

# Imprime o próximo documento
spooler.imprimir_documento()
spooler.imprimir_documento()
