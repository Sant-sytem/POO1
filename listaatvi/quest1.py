def calcular_area_triangulo():
 base = float(input ("infome o valor da base do triangulo:"))
 altura = float(input("infome a alatura do trinagulo:")) 
 return(base*altura)/2

def calcular_area_quadrado():
 lado= float(input("infome o lado do quadrado:"))
 return lado **2

def calcular_area_circulo():
 raio = float(input("infome o raio do circulo:"))
 return 3.14 * (raio**2)

def main ():
    while True:
        print("\nEscolha uma forma geometrica para calcular a area:")
        print("1. Triangulo")
        print("2. Quadrado")
        print("3. Circulo")
        print("4. Sair")

        escolha = input("Digite o numero correspondente a forma (ou 4 para sair): ")

        if escolha == "1":
            area = calcular_area_triangulo()
            print(f"A area do triângulo é: {area:.2f}")
        elif escolha == "2":
            area = calcular_area_quadrado()
            print(f"A area do quadrado é: {area:.2f}")
        elif escolha == "3":
            area = calcular_area_circulo()
            print(f"A area do círculo é: {area:.2f}")
        elif escolha == "4":
            print("Saindo do programa.")
            break
        else:
            print("Escolha inválida. Tente novamente.")


    main()