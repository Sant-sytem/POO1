import random

valorI = int(input("Digite o valor inicial:"))
valorF = int (input("Digite o valor final:"))
quant= int(input("Digite a quantidade:"))

sorteado= []

while quant > 0 and quant < valorF:
    x=random.randint(valorI,valorF)
    if x not in sorteado :
        sorteado.append(x)
        quant -=1
    if quant > valorF:
        print("Quantidade maior que o limite")
else:
        print(sorteado)
