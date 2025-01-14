quanto_ganho = int(input( "quanto ganho :"))
horas_trabalhadas= int( input( "horas trabalhadas: "))
salario= quanto_ganho * horas_trabalhadas
ir = salario * 0.11
inss = salario * 0.08
sindicato = salario * 0.05

print ('+ salario : R$ %.2f' %salario)
print ('- ir: R$ %.2f' %ir )
print ('- inss R$ %.2f' %inss )
print ('- sindicato: R$ %.2f' %sindicato )
print ('= salario iquido : R$ %.2f' %(salario - ir - inss - sindicato))
