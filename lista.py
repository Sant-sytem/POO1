par=[]
zero=[]
impar=[]


while True:
    num = int (input('Digite um numero:'))
    if num < 0:
     break
    elif num == 0:
        zero.append(num)
    elif num %2 == 0 :
       par.append (num)
    else:
       impar.append(num)
par.sort()
impar.sort()
resultado= par+zero+impar
print(resultado)


