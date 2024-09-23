horas = float(input('Por favor insira a quantidade de horas trabalhadas: \n'))
ganhos = float(input('Por favor insira o valor que voçê recebe por hora: \n'))
salario = horas*ganhos
imposto_de_renda = (salario*11)/100
inss = (salario*8)/100
sindc = (salario*5)/100
salario_liquido = salario - (imposto_de_renda+inss+sindc)
print(f'+ Salário Bruto : R$:{salario} \n')
print(f'- IR (11%) : R$: {imposto_de_renda} \n')
print(f'- INSS (8%) : R$: {inss} \n')
print(f'- Sindicato ( 5%) : R$: {sindc} \n')
print(f'= Salário Liquido : R$: {salario_liquido} \n')