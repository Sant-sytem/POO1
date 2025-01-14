num = int(input('Digite um decimal para converter em Binario: '))
lista = []

while num >= 1:
    resto = num % 2
    num = int(num // 2)

    lista.append(resto)

print(lista[-1::-1])