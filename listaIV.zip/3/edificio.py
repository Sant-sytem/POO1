from elevador import Elevador

class Edificio:
    def __init__(self, total_andares, capacidade_elevador):
        self.total_andares = total_andares
        self.elevador = Elevador(capacidade_elevador, total_andares)

    def get_elevador(self):
        return self.elevador
