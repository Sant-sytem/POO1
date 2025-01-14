class Televisao:
    def __init__(self, marca, canal_maximo=50, volume_maximo=100):
        self.marca = marca
        self.canal = 1  
        self.volume = 10  
        self.ligado = False
        self.canal_maximo = canal_maximo
        self.volume_maximo = volume_maximo

    def ligar(self):
        if not self.ligado:
            self.ligado = True
            print(f"A TV {self.marca} foi ligada.")
        else:
            print("A TV já está ligada.")

    def desligar(self):
        if self.ligado:
            self.ligado = False
            print(f"A TV {self.marca} foi desligada.")
        else:
            print("A TV já está desligada.")

    def __str__(self):
        status = "Ligada" if self.ligado else "Desligada"
        return f"\n=== TV {self.marca} ===\nStatus: {status}\nCanal: {self.canal}\nVolume: {self.volume}\n==================\n"
