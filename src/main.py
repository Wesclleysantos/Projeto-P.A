import tkinter as tk
from tkinter import colorchooser

ferramenta_atual = None     
cor_borda = "#000000"        
cor_preenchimento = "#FFFFFF"  


def atualizar_status():
    texto = (
        f"Ferramenta: {ferramenta_atual or 'Nenhuma'}    |    "
        f"Cor da borda: {cor_borda}    |    "
        f"Preenchimento: {cor_preenchimento}"
    )
    label_status.config(text=texto)


def selecionar_ferramenta(nome):
    global ferramenta_atual
    ferramenta_atual = nome
    atualizar_status()


def selecionar_cor_borda():
    global cor_borda
    cor = colorchooser.askcolor(title="Selecione a cor da borda")
    if cor and cor[1]:
        cor_borda = cor[1]
        preview_borda.config(bg=cor_borda)
        atualizar_status()


def selecionar_cor_preenchimento():
    global cor_preenchimento
    cor = colorchooser.askcolor(title="Selecione a cor de preenchimento")
    if cor and cor[1]:
        cor_preenchimento = cor[1]
        preview_preenchimento.config(bg=cor_preenchimento)
        atualizar_status()

def criar_barra_ferramentas(janela):
    frame_ferramentas = tk.Frame(janela, bd=1, relief=tk.RAISED)
    frame_ferramentas.pack(side=tk.TOP, fill=tk.X)

    tk.Label(frame_ferramentas, text="Ferramentas:").pack(side=tk.LEFT, padx=(5, 10))

    btn_retangulo = tk.Button(
        frame_ferramentas, text="Retângulo",
        command=lambda: selecionar_ferramenta("retangulo")
    )
    btn_retangulo.pack(side=tk.LEFT, padx=3, pady=3)

    btn_oval = tk.Button(
        frame_ferramentas, text="Oval",
        command=lambda: selecionar_ferramenta("oval")
    )
    btn_oval.pack(side=tk.LEFT, padx=3, pady=3)

    btn_circulo = tk.Button(
        frame_ferramentas, text="Círculo",
        command=lambda: selecionar_ferramenta("circulo")
    )
    btn_circulo.pack(side=tk.LEFT, padx=3, pady=3)

    return frame_ferramentas


def criar_seletor_cores(janela):
    global preview_borda, preview_preenchimento

    frame_cores = tk.Frame(janela, bd=1, relief=tk.RAISED)
    frame_cores.pack(side=tk.TOP, fill=tk.X)

    btn_cor_borda = tk.Button(
        frame_cores, text="Cor da Borda", command=selecionar_cor_borda
    )
    btn_cor_borda.pack(side=tk.LEFT, padx=(10, 3), pady=3)

    preview_borda = tk.Frame(
        frame_cores, width=25, height=25, bg=cor_borda,
        relief=tk.SUNKEN, bd=1
    )
    preview_borda.pack(side=tk.LEFT, padx=(0, 15), pady=3)

    
    btn_cor_preenchimento = tk.Button(
        frame_cores, text="Cor de Preenchimento", command=selecionar_cor_preenchimento
    )
    btn_cor_preenchimento.pack(side=tk.LEFT, padx=3, pady=3)

    preview_preenchimento = tk.Frame(
        frame_cores, width=25, height=25, bg=cor_preenchimento,
        relief=tk.SUNKEN, bd=1
    )
    preview_preenchimento.pack(side=tk.LEFT, padx=(0, 10), pady=3)


def criar_canvas(janela):
    canvas = tk.Canvas(janela, bg="white", cursor="cross")
    canvas.pack(side=tk.TOP, fill=tk.BOTH, expand=True, padx=5, pady=5)
    return canvas


def criar_status(janela):
    global label_status

    frame_status = tk.Frame(janela, bd=1, relief=tk.SUNKEN)
    frame_status.pack(side=tk.BOTTOM, fill=tk.X)

    label_status = tk.Label(
        frame_status,
        text="Ferramenta: Nenhuma    |    Cor da borda: #000000    |    Preenchimento: #FFFFFF",
        anchor="w"
    )
    label_status.pack(side=tk.LEFT, padx=10, pady=3)

def main():
    janela = tk.Tk()
    janela.title("Editor de Desenhos")
    janela.geometry("1000x700")

    criar_barra_ferramentas(janela)
    criar_seletor_cores(janela)
    criar_canvas(janela)
    criar_status(janela)

    janela.mainloop()


if __name__ == "__main__":
    main()