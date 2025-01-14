from agenda import Agenda

class App:
    @staticmethod
    def executar():
        agenda = Agenda(10)  

        while True:
            print("\n1. Nova Pessoa")
            print("2. Excluir Pessoa")
            print("3. Buscar Pessoa")
            print("4. Imprimir Agenda")
            print("5. Imprimir Pessoa (Indice)")
            print("6. Sair")
            opcao = int(input("Sua opção: "))

            if opcao == 1:
                nome = input("\nInforme o nome: ")
                idade = int(input("Informe a idade: "))
                altura = float(input("Informe a altura (use ponto em vez de virgula): "))
                agenda.armazena_pessoa(nome, idade, altura)

            elif opcao == 2:
                nome = input("\nInforme o nome a ser removido: ")
                agenda.remove_pessoa(nome)

            elif opcao == 3:
                nome = input("\nInforme o nome a ser pesquisado: ")
                indice = agenda.busca_pessoa(nome)
                if indice < 0:
                    print("\nA pessoa não foi encontrada")
                else:
                    print(f"\nA pessoa foi encontrada no indice: {indice}")

            elif opcao == 4:
                agenda.imprime_agenda()

            elif opcao == 5:
                index = int(input("\nInforme o indice desejado: "))
                agenda.imprime_pessoa(index)

            elif opcao == 6:
                print("\nSaindo...")
                break

            else:
                print("\nOpçao invalida\n")

if __name__ == "__main__":
    App.executar()

# site de apoio :https://www.arquivodecodigos.com.br/dicas/4122-java-exercicio-resolvido-de-java-poo-programacao-orientada-a-objetos-crie-uma-classe-agenda-que-pode-armazenar-10-pessoas-e-que-seja-capaz-de-realizar-as-seguintes-operacoes.html