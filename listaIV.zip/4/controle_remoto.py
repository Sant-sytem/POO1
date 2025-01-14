class ControleRemoto:
    def __init__(self, televisao):
        self.tv = televisao

    def aumentar_volume(self):
        if self.tv.ligado:
            if self.tv.volume < self.tv.volume_maximo:
                self.tv.volume += 1
                print(f"Volume aumentado para {self.tv.volume}.")
            else:
                print("O volume ja está no maximo!")
        else:
            print("A TV esta desligada. Ligue-a primeiro.")

    def diminuir_volume(self):
        if self.tv.ligado:
            if self.tv.volume > 0:
                self.tv.volume -= 1
                print(f"Volume diminuído para {self.tv.volume}.")
            else:
                print("O volume ja esta no minimo!")
        else:
            print("A TV esta desligada. Ligue-a primeiro.")

    def subir_canal(self):
        if self.tv.ligado:
            if self.tv.canal < self.tv.canal_maximo:
                self.tv.canal += 1
                print(f"Canal alterado para {self.tv.canal}.")
            else:
                print("Voce ja está no ultimo canal!")
        else:
            print("A TV esta desligada. Ligue-a primeiro.")

    def descer_canal(self):
        if self.tv.ligado:
            if self.tv.canal > 1:
                self.tv.canal -= 1
                print(f"Canal alterado para {self.tv.canal}.")
            else:
                print("Voce ja esta no primeiro canal!")
        else:
            print("A TV esta desligada. Ligue-a primeiro.")

    def trocar_canal(self, canal):
        if self.tv.ligado:
            if 1 <= canal <= self.tv.canal_maximo:
                self.tv.canal = canal
                print(f"Canal alterado para {self.tv.canal}.")
            else:
                print(f"Escolha um canal entre 1 e {self.tv.canal_maximo}.")
        else:
            print("A TV esta desligada. Ligue-a primeiro.")

    def consultar(self):
        print(self.tv)
