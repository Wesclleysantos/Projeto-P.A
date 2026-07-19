import json
from tkinter import filedialog


class Persistencia:

    def salvar(self, desenho):

        caminho = filedialog.asksaveasfilename(
            defaultextension=".json",
            filetypes=[("Arquivo JSON", "*.json")]
        )

        if not caminho:
            return

        figuras_json = []

        for figura in desenho.figuras:

            dados = {
                "versao": 1,
                "tipo": figura.__class__.__name__,
                "cor_borda": figura.cor_borda,
                "cor_preenchimento": figura.cor_preenchimento
}

            if hasattr(figura, "pontos"):
                dados["pontos"] = figura.pontos

            else:
                dados["x1"] = figura.x1
                dados["y1"] = figura.y1
                dados["x2"] = figura.x2
                dados["y2"] = figura.y2

            figuras_json.append(dados)

        with open(caminho, "w", encoding="utf-8") as arquivo:
            json.dump(figuras_json, arquivo, indent=4)