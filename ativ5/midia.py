from abc import ABC, abstractmethod

class Midia(ABC):
    def __init__(self, titulo, autor, disponivel):
        self.titulo = titulo
        self.autor = autor
        self.disponivel = disponivel  

    @abstractmethod
    def obter_info(self):
        pass

    @abstractmethod
    def verificar_disponibilidade(self):
        pass
