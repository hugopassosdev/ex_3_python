num_operacao = int(input("Insira a aoperação matemática: 1 Soma / 2 Subtração / 3 Multiplicação / 4 Divisão: "))



while(num_operacao != 0):

    def calculadora(num1, num2, num_operacao):
        if (num_operacao == 1): return num1 + num2
        elif (num_operacao == 2): return num1 - num2
        elif (num_operacao == 3): return num1 * num2
        elif(num_operacao == 4): return num1 / num2
        else: return 0
num1 = int(input("Insira o primeiro número: "))
num2 = int(input("Insira o segundo número: "))

resultado = calculadora(num1, num2, num_operacao)
print(resultado)