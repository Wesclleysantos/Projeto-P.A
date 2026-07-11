from tkinter import colorchooser


cor_borda = "#000000"          
cor_preenchimento = "#FFFFFF"  


def escolher_cor_borda():
    global cor_borda

    cor = colorchooser.askcolor(title="Escolha a cor da borda")

    if cor[1] is not None:
        cor_borda = cor[1]


def escolher_cor_preenchimento():
    global cor_preenchimento

    cor = colorchooser.askcolor(title="Escolha a cor do preenchimento")

    if cor[1] is not None:
        cor_preenchimento = cor[1]


def obter_cor_borda():
    return cor_borda


def obter_cor_preenchimento():
    return cor_preenchimento