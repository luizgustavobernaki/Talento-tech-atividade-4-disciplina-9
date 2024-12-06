from operacoes import adicionar, subtrair, multiplicar, dividir

def calculadora():
    print("Bem-vindo à Calculadora Simples!")
    print("Selecione a operação:")
    print("1. Adicionar")
    print("2. Subtrair")
    print("3. Multiplicar")
    print("4. Dividir")

    while True:
        escolha = input("Escolha uma opção (1/2/3/4 ou 'sair' para encerrar): ")

        if escolha.lower() == 'sair':
            print("Encerrando a calculadora. Até mais!")
            break

        if escolha in ['1', '2', '3', '4']:
            try:
                num1 = float(input("Digite o primeiro número: "))
                num2 = float(input("Digite o segundo número: "))

                if escolha == '1':
                    print(f"Resultado: {adicionar(num1, num2)}")
                elif escolha == '2':
                    print(f"Resultado: {subtrair(num1, num2)}")
                elif escolha == '3':
                    print(f"Resultado: {multiplicar(num1, num2)}")
                elif escolha == '4':
                    print(f"Resultado: {dividir(num1, num2)}")
            except ValueError:
                print("Por favor, insira números válidos.")
        else:
            print("Opção inválida. Tente novamente.")

# Executa o programa
if __name__ == "__main__":
    calculadora()
