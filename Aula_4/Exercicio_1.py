class EditorTexto:
    def __init__(self):
        self.texto = ""
        self.pilha = []

    def digitar(self, texto):
        # Adiciona o texto ao final
        self.texto += texto
        # Armazena a ação na pilha
        self.pilha.append(("digitar", texto))

    def apagar(self, quantidade):
        # Verifica se há caracteres suficientes
        if quantidade > len(self.texto):
            quantidade = len(self.texto)
        # Guarda o que foi apagado
        texto_apagado = self.texto[-quantidade:]
        self.texto = self.texto[:-quantidade]
        # Armazena a ação na pilha
        self.pilha.append(("apagar", texto_apagado))

    def substituir(self, antigo, novo):
        # Verifica se o texto antigo existe
        if antigo in self.texto:
            posicao = self.texto.find(antigo)
            # Guarda o texto original para poder desfazer
            self.texto = (
                self.texto[:posicao]
                + novo
                + self.texto[posicao + len(antigo):]
            )
            # Armazena a ação na pilha
            self.pilha.append(("substituir", posicao, antigo, novo))
        else:
            print("Texto não encontrado.")

    def desfazer(self):
        # Verifica se existem ações para desfazer
        if not self.pilha:
            print("Nenhuma ação para desfazer.")
            return
        # Remove estritamente a última ação (LIFO)
        acao = self.pilha.pop()

        if acao[0] == "digitar":
            texto_digitado = acao[1]
            self.texto = self.texto[:-len(texto_digitado)]

        elif acao[0] == "apagar":
            texto_apagado = acao[1]
            self.texto += texto_apagado

        elif acao[0] == "substituir":
            posicao, antigo, novo = acao[1], acao[2], acao[3]
            self.texto = (
                self.texto[:posicao]
                + antigo
                + self.texto[posicao + len(novo):]
            )
        print("Última ação desfeita.")

    def mostrar(self):
        print("Texto atual:", self.texto)


# Exemplo de utilização

editor = EditorTexto()

editor.digitar("Olá ")
editor.digitar("mundo")
editor.mostrar()

# Texto: Olá mundo

editor.apagar(5)
editor.mostrar()

# Texto: Olá 

editor.digitar("Python")
editor.mostrar()

# Texto: Olá Python

editor.substituir("Python", "Java")
editor.mostrar()

# Texto: Olá Java

editor.desfazer()

# Desfaz somente a última ação

editor.mostrar()

# Texto: Olá Python

editor.desfazer()

# Desfaz novamente a ação anterior

editor.mostrar()

# Texto: Olá 
