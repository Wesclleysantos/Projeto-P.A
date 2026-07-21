from tkinter import Frame
from tkinter import StringVar
from tkinter import SUNKEN
from tkinter import W

from tkinter import ttk


class Toolbar(Frame):

    def __init__(self, master):

        super().__init__(master)

        self.grid(row=0, column=0)

        self.ferramenta = StringVar()

        self._criar()

    def _criar(self):

        figuras = [
            "Linha",
            "Rabisco",
            "Retângulo",
            "Oval",
            "Círculo"
        ]

        ttk.Label(
            self,
            text="Figura:"
        ).grid(
            row=0,
            column=0,
            padx=5,
            pady=5,
            sticky=W
        )

        ttk.OptionMenu(
            self,
            self.ferramenta,
            figuras[0],
            *figuras
        ).grid(
            row=0,
            column=1,
            padx=5,
            pady=5
        )

        self.btn_borda = ttk.Button(
            self,
            text="Cor da borda"
        )

        self.btn_borda.grid(
            row=0,
            column=2,
            padx=5
        )

        self.preview_borda = Frame(
            self,
            width=25,
            height=25,
            relief=SUNKEN,
            bd=1,
            bg="black"
        )

        self.preview_borda.grid(
            row=0,
            column=3
        )

        self.btn_preenchimento = ttk.Button(
            self,
            text="Preenchimento"
        )

        self.btn_preenchimento.grid(
            row=0,
            column=4,
            padx=5
        )

        self.preview_preenchimento = Frame(
            self,
            width=25,
            height=25,
            relief=SUNKEN,
            bd=1,
            bg="white"
        )

        self.preview_preenchimento.grid(
            row=0,
            column=5
        )

        self.btn_salvar = ttk.Button(
            self,
            text="Salvar"
        )

        self.btn_salvar.grid(
            row=0,
            column=6,
            padx=5
        )

        self.btn_abrir = ttk.Button(
            self,
            text="Abrir"
        )

        self.btn_abrir.grid(
            row=0,
            column=7,
            padx=5
        )

    def atualizar_preview(self, borda, preenchimento):

        self.preview_borda.configure(bg=borda)

        self.preview_preenchimento.configure(
            bg=preenchimento
        )