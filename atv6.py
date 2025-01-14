num= int(input ("Digite um numero:"))
numcal= num
fatorial = 1

while( numcal> 0):
    fatorial = fatorial * numcal
    numcal -= 1

    print( "fatorial de ", num, "=", fatorial)
 