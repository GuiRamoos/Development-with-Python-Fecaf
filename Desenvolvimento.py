quantidade_rodas = int(input("Quantas rodas o veículo possui: "))
peso_bruto = float(input("Qual o peso do seu veículo: "))
quantidade_passageiros = int(input("Quantos passageiros estão no veículo: "))


if(quantidade_rodas == 3):{
    print("Categoria A")
}
elif(quantidade_rodas > 3 and peso_bruto <= 3500 and quantidade_passageiros <= 8):{
    print("Categoria B")
}
elif(quantidade_rodas > 4 and peso_bruto > 3500 and peso_bruto <= 6000 and quantidade_passageiros <= 8):{
    print("Categoria C")
}
elif(quantidade_rodas >= 4 and quantidade_passageiros >= 8 and peso_bruto <= 6000):{
    print("Categoria D")
}
elif(quantidade_rodas >= 4 and peso_bruto > 6000):{
    print("Categoria E")
}
else:{
    print("Categoria Inválida !!!")
}