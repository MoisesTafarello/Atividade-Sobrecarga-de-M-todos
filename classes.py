class Gerador_Relatorio:
    def gerar(self, *args, **kwargs):
        relatorio = ""

        if len(args) == 0:
            return "Ocorreu um erro: deve haver pelo menos um argumento para o corpo do texto."
            
        elif len(args) == 1:
            corpo = args[0]
            relatorio += f"{corpo}\n"

        elif len(args) == 2:
            titulo, corpo = args
            relatorio += f"{titulo}\n\n{corpo}\n\n"

        elif len(args) == 3:
            titulo, corpo, rodape = args
            relatorio += f"{titulo}\n\n{corpo}\n{rodape}\n"

        else:
            titulo = args[0]
            paragrafos = args[1:]
            relatorio += f"{titulo}\n\n"
            for i in paragrafos:
                relatorio += f"{i}\n\n"

            metadados = kwargs.get("metadados")
            if metadados:
                relatorio += f"\n-- Metadados --\n"
                for chave, valor in metadados.items():
                    relatorio += f"{chave.capitalize()}: {valor}\n"

            return relatorio

