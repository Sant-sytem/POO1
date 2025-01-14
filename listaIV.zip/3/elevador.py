class Elevador:
    def __init__(self, capacidade, total_andares):
        self.capacidade = capacidade
        self.total_andares = total_andares
        self.andar_atual = 0  
        self.pessoas_presentes = 0  

    def entra(self):
        if self.pessoas_presentes < self.capacidade:
            self.pessoas_presentes += 1
            print("Uma pessoa entrou no elevador.")
        else:
            print("O elevador esta cheio!")

    def sai(self):
        if self.pessoas_presentes > 0:
            self.pessoas_presentes -= 1
            print("Uma pessoa saiu do elevador.")
        else:
            print("O elevador esta vazio!")

    def sobe(self):
        if self.andar_atual < self.total_andares:
            self.andar_atual += 1
            print(f"O elevador subiu para o andar {self.andar_atual}.")
        else:
            print("O elevador já está no último andar!")

    def desce(self):
        if self.andar_atual > 0:
            self.andar_atual -= 1
            print(f"O elevador desceu para o andar {self.andar_atual}.")
        else:
            print("O elevador já está no terreo!")

    def status(self):
        print("\n=== Status do Elevador ===")
        print(f"Andar atual: {self.andar_atual}")
        print(f"Pessoas presentes: {self.pessoas_presentes}")
        print(f"Capacidade máxima: {self.capacidade}")
        print(f"Total de andares: {self.total_andares}")
        print("=======================\n")
