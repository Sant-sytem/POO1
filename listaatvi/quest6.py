ingresso = 5.00
l_max = 0
preco_max = 0
ingresso_vend_max = 0

while ingresso >= 1.00:
    ingresso_vend = 120 + ((5.00 - ingresso) / 0.50) * 26
    lucro = ingresso * ingresso_vend - 200.00

    if lucro > l_max:
        l_max = lucro
        preco_max = ingresso
        ingresso_vend_max = ingresso_vend

    print('Preço do ingresso: %.2f | Quantidade: %d | Lucro: %.2f\n' %(ingresso, ingresso_vend_max, lucro))

    ingresso -= 0.50

print('Lucro máximo: ', l_max)
print('Quantidade de ingressos vendidos: ', ingresso_vend_max)
print('Preço do ingresso: ', preco_max)