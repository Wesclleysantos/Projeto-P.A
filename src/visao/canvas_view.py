from tkinter import Canvas


class CanvasView(Canvas):

    def __init__(self, master):

        super().__init__(
            master,
            width=800,
            height=600,
            bg="white"
        )

        self.grid(
            row=1,
            column=0,
            columnspan=6,
            padx=10,
            pady=10
        )

    def limpar(self):
        self.delete("all")

    def desenhar(self, desenho):

        self.limpar()

        for figura in desenho.figuras:
            figura.desenhar(self)

    def desenhar_preview(self, desenho, figura):

        self.desenhar(desenho)

        if figura:
            figura.desenhar(self, preview=True)