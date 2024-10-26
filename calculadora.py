def somar(x, y):
    return x + y

def subtrair(x, y):
    return x - y

def multiplicar(x, y):
    return x * y

def dividir(x, y):
    #Tratamento de erros em divisão por zero

    if y == 0:
        return "Erro: Divisão por zero não é permitida"
    return x / y

def exibir_menu():
    print("Escolha a operação: ")
    print("1 - Somar")
    print("2 - Subtrair")
    print("3 - Multiplicar")
    print("4 - Dividir")
    print("0 - Sair")

def ler_numero(mensagem):
    while True:
        try:
            return float(input(mensagem))
        except ValueError:
            print("Entrada inválida! Por favor insira um número")

#Loop principal
while True:
    exibir_menu()
    escolha = input("Digite o número da operação (ou 0 para Sair)")

    if escolha == '0':
        print("Encerrando o programa")
        break

    if escolha in['1', '2', '3', '4']:        #Obter os números de entrada
        num1 = ler_numero("Digite o primeiro número")
        num2 = ler_numero("Digite o segundo número")

        if escolha == '1':
            print(f"Resultado:  {num1} + {num2} = {somar(num1, num2):.2f}")

        elif escolha == '2':
            print(f"Resultado: {num1} - {num2} = {subtrair(num1, num2):.2f}")

        elif escolha == '3':
            print(f"Resultado: {num1} * {num2} = {multiplicar(num1, num2):.2f}")

        elif escolha == '4':
            resultado = dividir(num1, num2)
            if isinstance(resultado, str): # Verifica se o resultado é uma mensagem de erro
                print(resultado)
            else:
                print(f"Resultado: {num1} / {num2} = {resultado:.2f}")

    else:
        print("Escolha inválida! Por favor, selecione uma opção válida")

