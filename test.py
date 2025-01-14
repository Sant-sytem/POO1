numr= []
add_num= lambda x: numr.insert(0,x) if x %2 == 0 and x !=0 else numr.append(x)

while True:
    num = int (input('Digite um numero:'))
    if num < 0:
     break
    elif num == 0:
        meio = len(numr)
        numr.insert(meio,0)
    else:
     add_num (num)
print( f"lista :{sorted (numr)}")
