def calculadora():
    while True:
        print("1: Soma")
        print("2: Subtração")
        print("3: Multiplicação")
        print("4: Divisão")
        print("0: Sair")

        opcao = input("Digite o número para a operação correspondente: ")

        if opcao == "0":
            print("Encerrando a calculadora...")
            break

        if opcao not in ["1", "2", "3", "4"]:
            print("Essa opção não existe.\n")
            continue

        valor1 = float(input("Digite o primeiro valor: "))
        valor2 = float(input("Digite o segundo valor: "))

        if opcao == "1":
            resultado = valor1 + valor2
            print("Resultado da soma:", resultado)
        elif opcao == "2":
            resultado = valor1 - valor2
            print("Resultado da subtração:", resultado)
        elif opcao == "3":
            resultado = valor1 * valor2
            print("Resultado da multiplicação:", resultado)
        elif opcao == "4":
            if valor2 == 0:
                print("Não é possível dividir por zero.\n")
                continue
            resultado = valor1 / valor2
            print("Resultado da divisão:", resultado)

        print()  

calculadora()