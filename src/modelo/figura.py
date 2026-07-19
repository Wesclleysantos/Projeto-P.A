from abc import ABC, abstractmethod


class Figura(ABC):
    """
    Classe base de todas as figuras.
    """

    def __init__(self, x, y, cor_borda, cor_preenchimento):

        self.x1 = x
        self.y1 = y

        self.x2 = x
        self.y2 = y

        self.cor_borda = cor_borda
        self.cor_preenchimento = cor_preenchimento

    def atualizar(self, x, y):
        """
        Atualiza o ponto final da figura.
        """

        self.x2 = x
        self.y2 = y

    @abstractmethod
    def desenhar(self, canvas, preview=False):
        """
        Cada figura desenha a si mesma.
        """
        pass

    @abstractmethod
    def contem(self, x, y):
        """
        Será usado na Entrega 5 para seleção.
        """
        pass

    def incompleta(self):
        """
        Verifica se a figura foi realmente desenhada.
        """

        return (
            self.x1 == self.x2
            and
            self.y1 == self.y2
        )