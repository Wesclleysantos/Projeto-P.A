from .figura import Figura


class Oval(Figura):

    def desenhar(self, canvas, preview=False):

        opcoes = {
            "outline": self.cor_borda,
            "fill": self.cor_preenchimento,
            "width": 2
        }

        if preview:
            opcoes["dash"] = (4, 2)

        canvas.create_oval(
            self.x1,
            self.y1,
            self.x2,
            self.y2,
            **opcoes
        )

    def contem(self, x, y):
        """
        Implementação simples.
        Na entrega da seleção podemos melhorar.
        """
        return (
            min(self.x1, self.x2) <= x <= max(self.x1, self.x2)
            and
            min(self.y1, self.y2) <= y <= max(self.y1, self.y2)
        )