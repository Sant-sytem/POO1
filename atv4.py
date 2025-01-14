tipo = input("digite A para alcool ou G para gasolina: ")
quant = int(input("digite a quantidade de litros: "))

if tipo == 'A':
    preco_comb = 3.45
    desconto_20 = 3
    desconto_20_mais = 5
else:
    preco_comb = 4.53
    desconto_20 = 4
    desconto_20_mais = 6

if quant <= 20:
    desconto = preco_comb * quant * desconto_20 / 100

    p_final = preco_comb * quant - desconto
else:
    desconto = preco_comb * 20 * desconto_20 / 100
    desconto = desconto + (quant - 20) * desconto_20_mais / 100

    p_final = preco_comb * quant - desconto

print("O total eh: ", p_final)