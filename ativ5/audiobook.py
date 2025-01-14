from midia import Midia

class AudioBook(Midia):
    def __init__(self, titulo, autor, duracao, disponivel):
        super().__init__(titulo, autor, disponivel)
        self.duracao = duracao

    def obter_info(self):
        return f"AudioBook: {self.titulo}, Autor: {self.autor}, Duração: {self.duracao} minutos"

    def verificar_disponibilidade(self):
        return self.disponivel  
