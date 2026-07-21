from tkinter import colorchooser

from modelo.desenho import Desenho
from modelo.gerenciador_cores import GerenciadorCores
from modelo.persistencia import Persistencia
from controlador.estados.estado_linha import EstadoLinha
from controlador.estados.estado_retangulo import EstadoRetangulo
from controlador.estados.estado_oval import EstadoOval
from controlador.estados.estado_circulo import EstadoCirculo
from controlador.estados.estado_rabisco import EstadoRabisco
from modelo.linha import Linha
from modelo.oval import Oval
from modelo.retangulo import Retangulo
from modelo.circulo import Circulo
from modelo.rabisco import Rabisco

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
        
        self.view.toolbar.btn_abrir.configure(
            command=self.abrir
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

    def trocar_estado(self, *args):

        ferramenta = self.view.toolbar.ferramenta.get()

        if ferramenta == "Linha":
            self.estado = EstadoLinha()

        elif ferramenta == "Rabisco":
            self.estado = EstadoRabisco()

        elif ferramenta == "Retângulo":
            self.estado = EstadoRetangulo()

        elif ferramenta == "Oval":
            self.estado = EstadoOval()

        elif ferramenta == "Círculo":
            self.estado = EstadoCirculo()
    
    def salvar(self):
        self.persistencia.salvar(self.desenho)

    def abrir(self):

        dados = self.persistencia.abrir()

        if dados is None:
            return
        
        self.desenho.limpar()

        for figura in dados:
            tipo = figura["tipo"]

            if tipo == "Linha":

                nova = Linha(
                    figura["x1"],
                    figura["y1"],
                    figura["cor_borda"],
                    figura["cor_preenchimento"]
                )

                nova.atualizar(
                    figura["x2"],
                    figura["y2"]
                )
            
            elif tipo == "Retangulo":

                nova = Retangulo(
                    figura["x1"],
                    figura["y1"],
                    figura["cor_borda"],
                    figura["cor_preenchimento"]
                )

                nova.atualizar(
                    figura["x2"],
                    figura["y2"]
                )

            elif tipo == "Oval":

                nova = Oval(
                    figura["x1"],
                    figura["y1"],
                    figura["cor_borda"],
                    figura["cor_preenchimento"]
                )

                nova.atualizar(
                    figura["x2"],
                    figura["y2"]
                )

            elif tipo == "Circulo":

                nova = Circulo(
                    figura["x1"],
                    figura["y1"],
                    figura["cor_borda"],
                    figura["cor_preenchimento"]
                )

                nova.atualizar(
                    figura["x2"],
                    figura["y2"]
                )

            elif tipo == "Rabisco":
                
                nova = Rabisco(
                    figura["pontos"][0][0],
                    figura["pontos"][0][1],
                    figura["cor_borda"],
                    figura["cor_preenchimento"]
                )

                nova.pontos = figura["pontos"]

            else:
                continue

            self.desenho.adicionar(nova)

            self.view.canvas.desenhar(

                self.desenho
                
            )
