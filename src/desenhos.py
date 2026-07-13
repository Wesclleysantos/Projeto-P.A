class GerenciadorDesenho:
    def __init__(self, gerenciador_cores):
        self.gerenciador_cores = gerenciador_cores

        self.figuras = []       # Todas as figuras já desenhadas
        self.figura_nova = None # Figura sendo desenhada no momento

    def iniciar(self, evento, ferramenta):
        if ferramenta is None:
            self.figura_nova = None
            return

        cor_borda = self.gerenciador_cores.obter_cor_borda()
        cor_preenchimento = self.gerenciador_cores.obter_cor_preenchimento()

        if ferramenta == "rabisco":
            self.figura_nova = (
                "rabisco", [(evento.x, evento.y)], cor_borda, cor_preenchimento
            )
        else:  # linha, retangulo, oval, circulo
            self.figura_nova = (
                ferramenta, (evento.x, evento.y, evento.x, evento.y),
                cor_borda, cor_preenchimento
            )

    def atualizar(self, evento, canvas, ferramenta):
        if self.figura_nova is None:
            return

        fig, values, cor_borda, cor_preenchimento = self.figura_nova

        if fig == "rabisco":
            values.append((evento.x, evento.y))
        else:
            values = (values[0], values[1], evento.x, evento.y)

        self.figura_nova = (fig, values, cor_borda, cor_preenchimento)

        canvas.delete("all")
        self.redesenhar_tudo(canvas)
        self.desenhar_figura(canvas, self.figura_nova, dash=(4, 2))

    def armazenar(self, evento, canvas, ferramenta):
        if self.figura_nova is not None and not self.incompleta(self.figura_nova):
            self.figuras.append(self.figura_nova)

        self.figura_nova = None

        canvas.delete("all")
        self.redesenhar_tudo(canvas)

    def redesenhar_tudo(self, canvas):
        for figura in self.figuras:
            self.desenhar_figura(canvas, figura)

    def desenhar_figura(self, canvas, figura, dash=None):
        fig, values, cor_borda, cor_preenchimento = figura

        if fig == "linha":
            opcoes = {"fill": cor_borda}
            if dash:
                opcoes["dash"] = dash
            canvas.create_line(values[0], values[1], values[2], values[3], **opcoes)

        elif fig == "rabisco":
            if len(values) > 1:
                opcoes = {"fill": cor_borda}
                if dash:
                    opcoes["dash"] = dash
                canvas.create_line(values, **opcoes)

        elif fig == "retangulo":
            opcoes = {"outline": cor_borda, "fill": cor_preenchimento, "width": 2}
            if dash:
                opcoes["dash"] = dash
            canvas.create_rectangle(values[0], values[1], values[2], values[3], **opcoes)

        elif fig == "oval":
            opcoes = {"outline": cor_borda, "fill": cor_preenchimento, "width": 2}
            if dash:
                opcoes["dash"] = dash
            canvas.create_oval(values[0], values[1], values[2], values[3], **opcoes)

        else:  # circulo
            xi, yi, xf, yf = values
            raio = ((xi - xf) ** 2 + (yi - yf) ** 2) ** 0.5
            opcoes = {"outline": cor_borda, "fill": cor_preenchimento, "width": 2}
            if dash:
                opcoes["dash"] = dash
            canvas.create_oval(xi - raio, yi - raio, xi + raio, yi + raio, **opcoes)

    def incompleta(self, figura):
        fig, values = figura[0], figura[1]

        if fig == "rabisco":
            return len(values) <= 1
        else:  # linha, retangulo, oval, circulo
            return (values[0], values[1]) == (values[2], values[3])