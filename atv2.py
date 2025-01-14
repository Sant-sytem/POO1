peso = float(input("peso :"))
execesso= 0 
multa = 0
if peso <= 50:
    print("execesso: %.2f" %execesso)
    print("multa:%.2f" %multa)
else: 
    execesso = peso - 50
    multa = execesso * 4.0
    
    print("execesso: %.2f" %execesso)
    print("multa:%.2f" %multa)
