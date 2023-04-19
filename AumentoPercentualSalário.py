cargo = input ('Entre com o código do cargo: ').upper ()
salario = float (input('Entre com o salário em R$: '))
if  (cargo == 'GER') :
    perc = 0.1
elif (cargo == 'ENG') :
    perc = 0.2
elif (cargo == 'TEC') :
    perc = 0.3
else:
    perc = 0.4
aumento = perc * salario
novosal = salario + aumento
print ('Salário antigo:  R$:',round(salario,2))
print ('Novo Salário: R$:',round(novosal,2))
print('Diferença: R$:',round(aumento,2))
