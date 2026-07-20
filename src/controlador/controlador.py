from tkinter import colorchooser

from modelo.desenho import Desenho
from modelo.gerenciador_cores import GerenciadorCores

from controlador.estados.estado_linha import EstadoLinha
from controlador.estados.estado_retangulo import EstadoRetangulo
from controlador.estados.estado_oval import EstadoOval
from controlador.estados.estado_circulo import EstadoCirculo
from controlador.estados.estado_rabisco import EstadoRabisco


from modelo.persistencia import Persistencia

class Controlador:


    def __init__(self, view):

        self.view = view

        self.desenho = Desenho()

        self.cores = GerenciadorCores()

        self.persistencia = Persistencia()

        self.figura_atual = None

        self.estado = EstadoLinha()

        self._ligar_eventos()

        self.trocar_estado()

        
            

    # -------------------------
    # Liga os eventos da View
    # -------------------------

    def _ligar_eventos(self):

        canvas = self.view.canvas

        canvas.bind("<ButtonPress-1>", self.mouse_press)
        canvas.bind("<B1-Motion>", self.mouse_move)
        canvas.bind("<ButtonRelease-1>", self.mouse_release)

        self.view.toolbar.ferramenta.trace_add(
            "write",
            self.trocar_estado
        )

        self.view.toolbar.btn_borda.configure(
            command=self.escolher_cor_borda
        )

        self.view.toolbar.btn_preenchimento.configure(
            command=self.escolher_cor_preenchimento
        )

        self.view.toolbar.btn_salvar.configure(
            command=self.salvar
)

    # -------------------------
    # Eventos do Mouse
    # -------------------------

    def mouse_press(self, event):

        self.estado.mouse_press(self, event)

    def mouse_move(self, event):

        self.estado.mouse_move(self, event)

    def mouse_release(self, event):

        self.estado.mouse_release(self, event)

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