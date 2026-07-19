import math

from .figura import Figura


class Circulo(Figura):

    def desenhar(self, canvas, preview=False):

        raio = math.sqrt(
            (self.x2 - self.x1) ** 2 +
            (self.y2 - self.y1) ** 2
        )

        opcoes = {
            "outline": self.cor_borda,
            "fill": self.cor_preenchimento,
            "width": 2
        }

        if preview:
            opcoes["dash"] = (4, 2)

        canvas.create_oval(
            self.x1 - raio,
            self.y1 - raio,
            self.x1 + raio,
            self.y1 + raio,
            **opcoes
        )

    def contem(self, x, y):

        raio = math.sqrt(
            (self.x2 - self.x1) ** 2 +
            (self.y2 - self.y1) ** 2
        )

        distancia = math.sqrt(
            (x - self.x1) ** 2 +
            (y - self.y1) ** 2
        )

        return distancia <= raio