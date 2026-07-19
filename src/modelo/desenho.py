class Desenho:

    def __init__(self):

        self.figuras = []

    def adicionar(self, figura):

        self.figuras.append(figura)

    def remover(self, figura):

        self.figuras.remove(figura)

    def limpar(self):

        self.figuras.clear()

    def desenhar(self, canvas):

        for figura in self.figuras:
            figura.desenhar(canvas)

    def quantidade(self):

        return len(self.figuras)

    def ultima(self):

        if self.figuras:
            return self.figuras[-1]

        return None