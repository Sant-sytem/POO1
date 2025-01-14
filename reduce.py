import functools as ft

def i(p,q):
    return p+q
numeros = [1,2,3,4]

n= ft.reduce(i,numeros)

print(n)
