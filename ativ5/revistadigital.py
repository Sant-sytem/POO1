from midia import Midia

class RevistaDigital(Midia):
    def __init__(self, titulo, autor, edicao, ano_publicacao, disponivel):
        super().__init__(titulo, autor, disponivel)
        self.edicao = edicao
        self.ano_publicacao = ano_publicacao

    def obter_info(self):
        return f"Revista Digital: {self.titulo}, autor:{self.autor}, edicao: {self.edicao}, Ano de Publicação: {self.ano_publicacao}"

    def verificar_disponibilidade(self):
        return self.disponivel
