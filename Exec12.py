prod = float(input('Qual o preço desse produto?  R$:'))
promo = prod * 5 / 100
final = prod - promo
print(f'O produto que custava R${prod :.2f}, na promoção com desconto de 5% vai passar a custar {final :.2f}')