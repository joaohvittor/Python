num1 = float(input('Insira o primeiro numero: \n'))
num2 = float(input('Insira o segundo numero: \n'))
num3 = float(input('Insira o terceiro numero: \n'))
if num1>num2 and num1>num3:
    print(f'{num1}')
elif num2>num1 and num2>num3:
    print(f'{num2}')
elif num3>num2 and num3>num1:
    print(f'{num3}') 
    
if num1<num2 and num1<num3:
    print(f'{num1}')
elif num2<num1 and num2<num3:
    print(f'{num2}')
elif num3<num2 and num3<num1:
    print(f'{num3}') 