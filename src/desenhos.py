import cores

xini = None
yini = None
xfim = None
yfim = None
raio = None

retangulos = []
ovais = []
circulos = []


def iniciar(evento):
    global xini, yini
    xini = evento.x
    yini = evento.y


def atualizar(evento, canvas, ferramenta):
    global xini, yini, xfim, yfim

    if ferramenta is None or xini is None:
        return

    xfim = evento.x
    yfim = evento.y

    canvas.delete("all")
    redesenhar_tudo(canvas)
    desenhar_atual(canvas, ferramenta, xini, yini, xfim, yfim)


def desenhar_atual(canvas, ferramenta, xi, yi, xf, yf):
    global raio

    cor_borda = cores.obter_cor_borda()
    cor_preenchimento = cores.obter_cor_preenchimento()

    if ferramenta == "oval":
        canvas.create_oval(
            xi, yi, xf, yf,
            outline=cor_borda, fill=cor_preenchimento, width=2
        )
    elif ferramenta == "circulo":
        raio = ((xi - xf) ** 2 + (yi - yf) ** 2) ** 0.5
        canvas.create_oval(
            xi - raio, yi - raio, xi + raio, yi + raio,
            outline=cor_borda, fill=cor_preenchimento, width=2
        )
    else:
        canvas.create_rectangle(
            xi, yi, xf, yf,
            outline=cor_borda, fill=cor_preenchimento, width=2
        )


def armazenar(evento, canvas, ferramenta):
    global xini, yini, xfim, yfim, raio

    if ferramenta is None or xini is None or xfim is None:
        return

    cor_borda = cores.obter_cor_borda()
    cor_preenchimento = cores.obter_cor_preenchimento()

    if ferramenta == "oval":
        ovais.append((xini, yini, xfim, yfim, cor_borda, cor_preenchimento))
    elif ferramenta == "circulo":
        circulos.append((
            xini - raio, yini - raio, xini + raio, yini + raio,
            cor_borda, cor_preenchimento
        ))
    else:
        retangulos.append((xini, yini, xfim, yfim, cor_borda, cor_preenchimento))

    canvas.delete("all")
    redesenhar_tudo(canvas)

    xini, yini, xfim, yfim = None, None, None, None


def redesenhar_tudo(canvas):
    for xi, yi, xf, yf, cor_borda, cor_preenchimento in retangulos:
        canvas.create_rectangle(
            xi, yi, xf, yf, outline=cor_borda, fill=cor_preenchimento, width=2
        )

    for xi, yi, xf, yf, cor_borda, cor_preenchimento in ovais:
        canvas.create_oval(
            xi, yi, xf, yf, outline=cor_borda, fill=cor_preenchimento, width=2
        )

    for xi, yi, xf, yf, cor_borda, cor_preenchimento in circulos:
        canvas.create_oval(
            xi, yi, xf, yf, outline=cor_borda, fill=cor_preenchimento, width=2
        )