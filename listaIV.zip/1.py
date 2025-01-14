from datetime import date, datetime

class Pessoa:
    def __init__(self, nome: str, data_nascimento: str, altura: float):
        self.__nome = nome
        self.__data_nascimento = datetime.strptime(data_nascimento, '%Y-%m-%d').date()
        self.__altura = altura

    def get_nome(self):
        return self.__nome

    def set_nome(self, nome):
        self.__nome = nome

    def get_data_nascimento(self):
        return self.__data_nascimento

    def set_data_nascimento(self, data_nascimento: str):
        self.__data_nascimento = datetime.strptime(data_nascimento, '%Y-%m-%d').date()

    def get_altura(self):
        return self.__altura

    def set_altura(self, altura: float):
        self.__altura = altura

    def imprimir_dados(self):
        print(f"Nome: {self.__nome}")
        print(f"Data de Nascimento: {self.__data_nascimento.strftime('%d/%m/%Y')}")
        print(f"Altura: {self.__altura:.2f} m")

    def calcular_idade(self):
        hoje = date.today()
        idade = hoje.year - self.__data_nascimento.year
        if (hoje.month, hoje.day) < (self.__data_nascimento.month, self.__data_nascimento.day):
            idade -= 1
        return idade


if __name__ == "__main__":
    p = Pessoa(nome="Patrick", data_nascimento="2001-08-08", altura=1.67)

    p.imprimir_dados()
    print(f"Idade: {p.calcular_idade()} anos")
