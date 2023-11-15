def calculadora(num1, num2, num_operacao):
    if (num_operacao == 1): return num1 + num2
    elif (num_operacao == 2): return num1 - num2
    elif (num_operacao == 3): return num1 * num2
    elif (num_operacao == 4): return num1 / num2
    else: return 0

calculadora_on_off = True

while(calculadora_on_off == True):
    num_operacao = int(input('Escolha uma das operações abaixo\n 1: Soma\n 2: Subtração\n 3: Multiplicação\n 4: Divisão\n 0: Sair\n'))
    if(num_operacao < 0 or num_operacao > 4):
        print('Essa opção não existe')
    elif(num_operacao == 0):
        calculadora_on_off = False
    else:
        num1 = int(input("Insira o primeiro número: "))
        num2 = int(input("Insira o segundo número: "))
        resultado = calculadora(num1, num2, num_operacao)
        print(f"A operação entre {num1} e {num2} obeteve o resultado {resultado}")