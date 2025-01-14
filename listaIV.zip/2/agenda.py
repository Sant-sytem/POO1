from pessoa import Pessoa

class Agenda:
    def __init__(self, quantidade):
        self.pessoas = [None] * quantidade

    def armazena_pessoa(self, nome, idade, altura):
        cadastrado = False
        for i in range(len(self.pessoas)):
            if self.pessoas[i] is None:
                self.pessoas[i] = Pessoa(nome, idade, altura)
                cadastrado = True
                break

        if cadastrado:
            print("\nCadastro efetuado com sucesso")
        else:
            print("\nNão foi possível cadastrar. Agenda cheia")

    def remove_pessoa(self, nome):
        excluido = False
        for i in range(len(self.pessoas)):
            if self.pessoas[i] is not None and self.pessoas[i].nome == nome:
                self.pessoas[i] = None
                excluido = True
                break

        if excluido:
            print("\nPessoa removida com sucesso")
        else:
            print("\nNao foi possível remover. Pessoa não encontrada.")

    def busca_pessoa(self, nome):
        for i in range(len(self.pessoas)):
            if self.pessoas[i] is not None and self.pessoas[i].nome == nome:
                return i
        return -1

    def imprime_agenda(self):
        for pessoa in self.pessoas:
            if pessoa is not None:
                pessoa.imprimir_dados()
                print()

    def imprime_pessoa(self, index):
        if index < 0 or index >= len(self.pessoas) or self.pessoas[index] is None:
            print("\nIndice invalido ou pessoa inexistente.")
        else:
            self.pessoas[index].imprimir_dados()
 
 #site de apoio: https://www.arquivodecodigos.com.br/dicas/4122-java-exercicio-resolvido-de-java-poo-programacao-orientada-a-objetos-crie-uma-classe-agenda-que-pode-armazenar-10-pessoas-e-que-seja-capaz-de-realizar-as-seguintes-operacoes.html