from tkinter import Tk

from visao.janela import Janela
from controlador.controlador import Controlador


def main():

    # Cria a janela principal
    root = Tk()

    # Instancia a View
    janela = Janela(root)

    # Instancia o Controller
    controlador = Controlador(janela)

    # Evita aviso de variável não utilizada
    _ = controlador

    # Inicia a aplicação
    root.mainloop()


if __name__ == "__main__":
    main()