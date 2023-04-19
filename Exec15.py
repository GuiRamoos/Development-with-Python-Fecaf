d = float(input('Quantos dias alugado?  '))
km = float(input('Quantos Km rodados?  '))
dia = d * 60
kmr = km * 0.15
tp = dia + kmr
print(f'O total a pagar é de R${tp}')