import math

co = float(input('Comprimento do Cateto oposto:  '))
ca = float(input('Comprimento do Cateto adjacente:  '))
h = math.hypot(co,ca)
print(f'A hipotenusa vai medir: {h}')