def obter_ano():
    while True:
        try:
            ano = int(input("Digite o ano de nascimento (entre 1922 e 2021): "))
            if 1922 <= ano <= 2021:
                return ano
            else:
                print("Ano fora do intervalo válido.")
        except ValueError:
            print("Digite um valor numérico válido.")

def calcular_idade(nome, ano_nascimento):
    ano_atual = 2022
    idade = ano_atual - ano_nascimento
    print("\nNome:", nome)
    print("Idade:", idade, "anos")

def main():
    nome = input("Digite o nome completo: ")
    ano_nascimento = obter_ano()
    calcular_idade(nome, ano_nascimento)

if __name__ == "__main__":
    main()