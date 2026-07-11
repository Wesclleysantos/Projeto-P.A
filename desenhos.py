import tkinter as tk

def interface(janela):
    #Criação do canvas
    canvas = tk.Canvas(janela, bg="white", width=600,height=600)
    canvas.pack(fill=tk.BOTH, expand=True)

    return canvas
    
#pega as coordenada iniciais do clique
def inicial(evento):
    global xini, yini
    xini = evento.x
    yini = evento.y

#pega e atualiza as coordenadas finais, limpa o canvas e recobra desenhos já feitos e cria novos
def atualizar(evento):
    global xini, yini, xfim, yfim, canva, retangulo, circulos

    xfim = evento.x
    yfim = evento.y

    canva.delete("all")
    recuperar(canva, retangulo, circulos)
    desenhar_atual(canva, xini, yini, xfim, yfim)

#desenha as formas 
def desenhar_atual(tela, xini, yini, xfim, yfim):
    global forma, raio, canva
    if forma == "oval":
        tela.create_oval(xini, yini, xfim, yfim)

    elif forma == "circulo":
        raio = ((xini - xfim) ** 2 + (yini - yfim) ** 2) ** 0.5

        tela.create_oval(xini - raio, yini - raio, xini + raio, yini + raio)

    else:
        tela.create_rectangle(xini, yini, xfim, yfim)

#armazena as formas para adicionar no canvas
def armazenar(_):
    global circulos, retangulo, forma, xini, yini, xfim, yfim, raio

    if forma == "oval":
        circulos.append((xini, yini, xfim, yfim))

    elif forma == "circulo":
        circulos.append((xini - raio, yini - raio, xini + raio, yini + raio))

    else:
        retangulo.append((xini, yini, xfim, yfim))

#adiciona as formas já feitas no canvas
def recuperar(tela, retangulo, circulos):

    for xi,yi,xf,yf in retangulo:
        tela.create_rectangle(xi,yi,xf,yf)

    for xi,yi,xf,yf in circulos:
        tela.create_oval(xi,yi,xf,yf)

      
janela = tk.Tk()
janela.geometry("600x600")

#variáveis para posições
xini = None
yini = None
xfim = None
yfim = None
raio = None

#nome da forma a ser criada
forma = "circulo"

#ovais e retangulos no canvas
retangulo = []
circulos = []

#interface principal
canva = interface(janela)

#eventos
canva.bind("<ButtonPress-1>", inicial)
canva.bind("<B1-Motion>", atualizar)
canva.bind("<ButtonRelease-1>", armazenar)

janela.mainloop()