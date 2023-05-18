#Projeto - ímpar ou Par
while True:
    try:
        valor = int(input("Digite um valor: "))
        if valor % 2 == 0:
            print('Número Par')
        else:
            print('Número ímpar')
    except: 
        print('Digite Apenas Números')   
