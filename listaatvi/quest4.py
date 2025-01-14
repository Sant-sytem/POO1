def primo(numero):
    mult = 0

    for count in range(2, numero):
        if numero % count == 0:
            mult += 1
    
    if mult == 0:
        return True
    else:
        return False

num1 = int(input('Insira um numero: '))
num2 = int(input('Insira outro numero: '))

aux = 0

for n in range(num1, num2+1):
    if primo(n) == True:
        print(n)
        
        aux += 1
    elif aux == 0:
        print('Não existe nenhum número primo dentro desse intervalo.')