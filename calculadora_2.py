num_operacao = int(input("Escolha uma das operações abaixo\n 1: Soma\n 2: Subtração\n 3: Multiplicação\n 4: Divisão\n 0: Sair\n"))
num1 = int(input("Insira o primeiro número: "))
num2 = int(input("Insira o segundo número: "))

def calculadora(num1, num2, num_operacao):
    if (num_operacao == 1): return num1 + num2
    elif (num_operacao == 2): return num1 - num2
    elif (num_operacao == 3): return num1 * num2
    elif (num_operacao == 4): return num1 / num2
    elif (num_operacao == 5): print('Sair')
    else: return print('Essa opção não existe.')

resultado = calculadora(num1, num2, num_operacao)
print(resultado)