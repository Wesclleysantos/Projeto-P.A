from .figura import Figura


class Linha(Figura):

    def desenhar(self, canvas, preview=False):

        opcoes = {
            "fill": self.cor_borda,
            "width": 2
        }

        if preview:
            opcoes["dash"] = (4, 2)

        canvas.create_line(
            self.x1,
            self.y1,
            self.x2,
            self.y2,
            **opcoes
        )

    def contem(self, x, y):
        """
        Será implementado depois usando a função
        distancia() fornecida pelo professor.
        """

        return False