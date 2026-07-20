from controlador.estados.estado import Estado
from modelo.circulo import Circulo


class EstadoCirculo(Estado):

    def mouse_press(self, controlador, event):

        controlador.figura_atual = Circulo(
            event.x,
            event.y,
            controlador.cores.obter_cor_borda(),
            controlador.cores.obter_cor_preenchimento()
        )

    def mouse_move(self, controlador, event):

        if controlador.figura_atual is None:
            return

        controlador.figura_atual.atualizar(
            event.x,
            event.y
        )

        controlador.view.canvas.desenhar_preview(
            controlador.desenho,
            controlador.figura_atual
        )

    def mouse_release(self, controlador, event):

        if controlador.figura_atual is None:
            return

        if not controlador.figura_atual.incompleta():

            controlador.desenho.adicionar(
                controlador.figura_atual
            )

        controlador.figura_atual = None

        controlador.view.canvas.desenhar(
            controlador.desenho
        )