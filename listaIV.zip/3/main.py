from edificio import Edificio

def main():
    print("=== Bem-vindo ao Sistema do Elevador ===")
    capacidade = int(input("Informe a capacidade do elevador: "))
    total_andares = int(input("Informe o total de andares (sem contar o térreo): "))

    edificio = Edificio(total_andares, capacidade)
    elevador = edificio.get_elevador()

    while True:
        print("\nMenu do Elevador:")
        print("1. Entrar uma pessoa")
        print("2. Sair uma pessoa")
        print("3. Subir um andar")
        print("4. Descer um andar")
        print("5. Mostrar status do elevador")
        print("6. Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            elevador.entra()
        elif opcao == "2":
            elevador.sai()
        elif opcao == "3":
            elevador.sobe()
        elif opcao == "4":
            elevador.desce()
        elif opcao == "5":
            elevador.status()
        elif opcao == "6":
            print("Encerrando o programa...")
            break
        else:
            print("Opção inválida! Tente novamente.")


if __name__ == "__main__":
    main()
 

# site de apoio : https://www.guj.com.br/t/classes/375768