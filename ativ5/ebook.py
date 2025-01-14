from midia import Midia
class Ebook(Midia):
    def __init__(self, titulo, autor, formato, disponivel):
        super().__init__(titulo, autor, disponivel)
        self._formato=formato

    @property
    def formato(self):
        return self._formato
    
    def obter_info(self):
        return f"Ebook-titulo{self.titulo}, autor:{self.autor}, formato:{self.formato}"

    def verificar_disponibilidade(self):
        return self.disponivel
    

