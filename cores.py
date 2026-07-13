from tkinter import colorchooser


class GerenciadorCores:
    def __init__(self):
        self.cor_borda = "#000000"
        self.cor_preenchimento = "#FFFFFF"

    def escolher_cor_borda(self):
        cor = colorchooser.askcolor(title="Escolha a cor da borda")

        if cor[1] is not None:
            self.cor_borda = cor[1]

    def escolher_cor_preenchimento(self):
        cor = colorchooser.askcolor(title="Escolha a cor do preenchimento")

        if cor[1] is not None:
            self.cor_preenchimento = cor[1]

    def obter_cor_borda(self):
        return self.cor_borda

    def obter_cor_preenchimento(self):
        return self.cor_preenchimento