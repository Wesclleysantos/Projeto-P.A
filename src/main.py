from tkinter import *
from tkinter import ttk

from cores import GerenciadorCores
from desenhos import GerenciadorDesenho


class EditorDesenho:
    MAPA_FERRAMENTAS = {
        "Linha": "linha",
        "Rabisco": "rabisco",
        "Retângulo": "retangulo",
        "Oval": "oval",
        "Círculo": "circulo",
    }

    def __init__(self, root):
        self.root = root
        self.frame = Frame(root)

        self.gerenciador_cores = GerenciadorCores()
        self.gerenciador_desenho = GerenciadorDesenho(self.gerenciador_cores)

        # Widgets que precisam ser acessados por outros métodos
        self.tipo_figura_var = None
        self.preview_borda = None
        self.preview_preenchimento = None
        self.canvas = None

        self._criar_widgets()
        self._associar_eventos()

        self.frame.pack()

    def _criar_widgets(self):
        paddings = {"padx": 5, "pady": 5}

        label = ttk.Label(self.frame, text="Figura:")
        label.grid(column=0, row=0, sticky=W, **paddings)

        self.tipo_figura_var = StringVar(self.root)
        tipos = list(self.MAPA_FERRAMENTAS.keys())
        option_menu = ttk.OptionMenu(
            self.frame, self.tipo_figura_var, tipos[0], *tipos
        )
        option_menu.grid(column=1, row=0, sticky=W, **paddings)

        btn_cor_borda = ttk.Button(
            self.frame, text="Cor da Borda", command=self.selecionar_cor_borda
        )
        btn_cor_borda.grid(column=2, row=0, sticky=W, **paddings)

        self.preview_borda = Frame(
            self.frame, width=25, height=25,
            bg=self.gerenciador_cores.obter_cor_borda(),
            relief=SUNKEN, bd=1
        )
        self.preview_borda.grid(column=3, row=0, sticky=W, **paddings)

        btn_cor_preenchimento = ttk.Button(
            self.frame, text="Cor de Preenchimento",
            command=self.selecionar_cor_preenchimento
        )
        btn_cor_preenchimento.grid(column=4, row=0, sticky=W, **paddings)

        self.preview_preenchimento = Frame(
            self.frame, width=25, height=25,
            bg=self.gerenciador_cores.obter_cor_preenchimento(),
            relief=SUNKEN, bd=1
        )
        self.preview_preenchimento.grid(column=5, row=0, sticky=W, **paddings)

        self.canvas = Canvas(self.frame, bg="white", width=600, height=600)
        self.canvas.grid(column=0, row=1, columnspan=6, sticky=W, **paddings)

    def _associar_eventos(self):
        self.canvas.bind("<ButtonPress-1>", self._on_press)
        self.canvas.bind("<B1-Motion>", self._on_motion)
        self.canvas.bind("<ButtonRelease-1>", self._on_release)

    def _on_press(self, evento):
        self.gerenciador_desenho.iniciar(evento, self.obter_ferramenta())

    def _on_motion(self, evento):
        self.gerenciador_desenho.atualizar(evento, self.canvas, self.obter_ferramenta())

    def _on_release(self, evento):
        self.gerenciador_desenho.armazenar(evento, self.canvas, self.obter_ferramenta())

    def obter_ferramenta(self):
        return self.MAPA_FERRAMENTAS[self.tipo_figura_var.get()]

    def selecionar_cor_borda(self):
        self.gerenciador_cores.escolher_cor_borda()
        self.preview_borda.config(bg=self.gerenciador_cores.obter_cor_borda())

    def selecionar_cor_preenchimento(self):
        self.gerenciador_cores.escolher_cor_preenchimento()
        self.preview_preenchimento.config(
            bg=self.gerenciador_cores.obter_cor_preenchimento()
        )


def main():
    root = Tk()
    root.title("Editor de Desenhos")
    EditorDesenho(root)
    root.mainloop()


if __name__ == "__main__":
    main()