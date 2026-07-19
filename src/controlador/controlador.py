from tkinter import colorchooser

from modelo.desenho import Desenho
from modelo.gerenciador_cores import GerenciadorCores

from modelo.linha import Linha
from modelo.retangulo import Retangulo
from modelo.oval import Oval
from modelo.circulo import Circulo
from modelo.rabisco import Rabisco


class Controlador:

    MAPA = {
        "Linha": Linha,
        "Rabisco": Rabisco,
        "Retângulo": Retangulo,
        "Oval": Oval,
        "Círculo": Circulo
    }

    def __init__(self, view):

        self.view = view

        self.desenho = Desenho()

        self.cores = GerenciadorCores()

        self.figura_atual = None

        self._ligar_eventos()

    # -------------------------
    # Liga os eventos da View
    # -------------------------

    def _ligar_eventos(self):

        canvas = self.view.canvas

        canvas.bind("<ButtonPress-1>", self.mouse_press)
        canvas.bind("<B1-Motion>", self.mouse_move)
        canvas.bind("<ButtonRelease-1>", self.mouse_release)

        self.view.toolbar.btn_borda.configure(
            command=self.escolher_cor_borda
        )

        self.view.toolbar.btn_preenchimento.configure(
            command=self.escolher_cor_preenchimento
        )

    # -------------------------
    # Eventos do Mouse
    # -------------------------

    def mouse_press(self, event):

        classe = self.MAPA[
            self.view.toolbar.ferramenta.get()
        ]

        self.figura_atual = classe(
            event.x,
            event.y,
            self.cores.obter_cor_borda(),
            self.cores.obter_cor_preenchimento()
        )

    def mouse_move(self, event):

        if self.figura_atual is None:
            return

        self.figura_atual.atualizar(
            event.x,
            event.y
        )

        self.view.canvas.desenhar_preview(
            self.desenho,
            self.figura_atual
        )

    def mouse_release(self, event):

        if self.figura_atual is None:
            return

        if not self.figura_atual.incompleta():

            self.desenho.adicionar(
                self.figura_atual
            )

        self.figura_atual = None

        self.view.canvas.desenhar(
            self.desenho
        )

    # -------------------------
    # Cores
    # -------------------------

    def escolher_cor_borda(self):

        cor = colorchooser.askcolor()

        if cor[1]:

            self.cores.cor_borda = cor[1]

            self.view.toolbar.atualizar_preview(
                self.cores.obter_cor_borda(),
                self.cores.obter_cor_preenchimento()
            )

    def escolher_cor_preenchimento(self):

        cor = colorchooser.askcolor()

        if cor[1]:

            self.cores.cor_preenchimento = cor[1]

            self.view.toolbar.atualizar_preview(
                self.cores.obter_cor_borda(),
                self.cores.obter_cor_preenchimento()
            )