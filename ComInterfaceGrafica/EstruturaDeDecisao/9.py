num1 = float(input('Insira o primeiro número: \n'))
num2 = float(input('Insira o segundo número: \n'))
num3 = float(input('Insira o terceiro número: \n'))
if num1 < num3:
    num1, num3 = num3, num1
elif num1 < num2:
    num1, num2 = num2, num1
elif num2 < num3:
    num2, num3 = num3, num2
print(f'A ordem decrescente é {num1}{num2}{num3}')