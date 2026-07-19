from .figura import Figura


class Rabisco(Figura):

    def __init__(self, x, y, cor_borda, cor_preenchimento):

        super().__init__(x, y, cor_borda, cor_preenchimento)

        self.pontos = [(x, y)]

    def atualizar(self, x, y):
        self.pontos.append((x, y))

    def desenhar(self, canvas, preview=False):

        if len(self.pontos) < 2:
            return

        opcoes = {
            "fill": self.cor_borda,
            "width": 2
        }

        if preview:
            opcoes["dash"] = (4, 2)

        canvas.create_line(
            self.pontos,
            **opcoes
        )

    def contem(self, x, y):
        return False

    def incompleta(self):
        return len(self.pontos) < 2