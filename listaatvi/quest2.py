# fatorial iterativo 
def calcular_fatorial(numero):
    resultado = 1
    for i in range(1, numero + 1):
        resultado *= i
    return resultado

numero = int(input("Digite um numero"))
resultado = calcular_fatorial(numero)
print("O fatorial de", numero, "eh", resultado)

# fatorial recusrivo
def calcular_fatorial(numero):
    if numero == 1:
        return 1
    else:
        return numero * calcular_fatorial(numero - 1)

numero = int(input("Digite um numero"))
resultado = calcular_fatorial(numero)
print("O fatorial de", numero, "eh", resultado)