salario = float(input('Insira o seu salario: \n'))
aumento1 = (salario*20)/100
novo_salario1 = salario+aumento1
aumento2 = (salario*15)/100
novo_salario2 = salario+aumento2
aumento3 = (salario*10)/100
novo_salario3 = salario+aumento3
aumento4 = (salario*5)/100
novo_salario4 = salario+aumento4
if salario <= 280:
    print(f'Seu salario de R${salario} sofreu um reajuste de 20% e passará a ser de R${novo_salario1} \n')
elif salario >= 280 and salario <= 700:
    print(f'Seu salario de R${salario} sofreu um reajuste de 15% e passará a ser de R${novo_salario2} \n')
elif salario >= 700 and salario <= 1500:
    print(f'Seu salario de R${salario} sofreu um reajuste de 10% e passará a ser de R${novo_salario3} \n')    
elif salario >= 1500:
    print(f'Seu salario de R${salario} sofreu um reajuste de 5% e passará a ser de R${novo_salario4} \n')    
        