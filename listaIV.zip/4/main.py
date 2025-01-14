from televisao import Televisao
from controle_remoto import ControleRemoto

def main():
    print("=== Bem-vindo ao Controle Remoto ===")
    marca_tv = input("Informe a marca da TV: ")
    tv = Televisao(marca_tv)
    controle = ControleRemoto(tv)

    while True:
        print("\nMenu:")
        print("1. Ligar a TV")
        print("2. Desligar a TV")
        print("3. Aumentar Volume")
        print("4. Diminuir Volume")
        print("5. Subir Canal")
        print("6. Descer Canal")
        print("7. Trocar para um Canal Específico")
        print("8. Consultar Status da TV")
        print("9. Sair")
        
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            tv.ligar()
        elif opcao == "2":
            tv.desligar()
        elif opcao == "3":
            controle.aumentar_volume()
        elif opcao == "4":
            controle.diminuir_volume()
        elif opcao == "5":
            controle.subir_canal()
        elif opcao == "6":
            controle.descer_canal()
        elif opcao == "7":
            try:
                canal = int(input("Informe o canal desejado: "))
                controle.trocar_canal(canal)
            except ValueError:
                print("Digite um número valido.")
        elif opcao == "8":
            controle.consultar()
        elif opcao == "9":
            print("Encerrando o programa...")
            break
        else:
            print("Opção invalida. Tente novamente.")

if __name__ == "__main__":
    main()
