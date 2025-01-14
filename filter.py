def par (n):
    return n %2== 0 and n !=0
def impar(n):
    return n %2 !=0
def zero(n):
    return n==0
lista=[]
while True:
    num=int(input ("Digite um numero:"))
    if num < 0:
        break
    else:
        lista.append(num)
parN= filter(par,lista)
imparN= filter(impar,lista)
zeroN= filter(zero,lista)
a=list(parN)
b=list(imparN)
c=list(zeroN)
print(a+c+b)

