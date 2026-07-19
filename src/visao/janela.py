from tkinter import Tk

from .toolbar import Toolbar
from .canvas_view import CanvasView


class Janela:

    def __init__(self, root: Tk):

        self.root = root

        self.root.title("Editor de Desenhos")
        self.root.geometry("900x700")

        # Barra superior
        self.toolbar = Toolbar(root)

        # Área de desenho
        self.canvas = CanvasView(root)