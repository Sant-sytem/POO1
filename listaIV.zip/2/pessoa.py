class Pessoa:
    def __init__(self, nome=None, idade=None, altura=None):
        self.nome = nome
        self.idade = idade
        self.altura = altura

    def imprimir_dados(self):
        print(f"Nome: {self.nome}\nIdade: {self.idade}\nAltura: {self.altura}")


# site de apoio : https://www.arquivodecodigos.com.br/dicas/4122-java-exercicio-resolvido-de-java-poo-programacao-orientada-a-objetos-crie-uma-classe-agenda-que-pode-armazenar-10-pessoas-e-que-seja-capaz-de-realizar-as-seguintes-operacoes.html