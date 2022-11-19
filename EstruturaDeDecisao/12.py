ganhos = float(input('Insira quanto voçê ganha por hora: \n'))
horast = float(input("Insira quantas horas voçê trabalha por mês: \n"))
salario = horast*ganhos
ir = 0
inss = (salario*10)/100
fgts = (salario*11)/100
total_desc = (ir+inss+fgts)
salario_liquid = salario - total_desc

salario2 = horast*ganhos
ir2 = (salario2*5)/100
inss2 = (salario2*10)/100
fgts2 = (salario2*11)/100
total_desc2 = (ir2+inss2+fgts2)
salario_liquid2 = salario2 - total_desc2

salario3 = horast*ganhos
ir3 = (salario3*5)/100
inss3 = (salario3*10)/100
fgts3 = (salario3*11)/100
total_desc3 = (ir3+inss3+fgts3)
salario_liquid3 = salario3 - total_desc3

salario4 = horast*ganhos
ir4 = (salario4*5)/100
inss4 = (salario4*10)/100
fgts4 = (salario4*11)/100
total_desc4 = (ir4+inss4+fgts4)
salario_liquid4 = salario4 - total_desc4




if salario <= 900:
       print(f' Salário Bruto:                  : R$ {salario} ')
       print(f' (-) IR (5%)                     :  {ir}   ')
       print(f' (-) INSS ( 10%)                 : R$  {inss} ')
       print(f' FGTS (11%)                      : R$  {fgts} ')
       print(f' Total de descontos              : R$  {total_desc} ')
       print(f' Salário Liquido                 : R$  {salario_liquid} ')
elif salario >= 900 and salario<= 1500:
       print(f' Salário Bruto: (                : R$ {salario} ')
       print(f' (-) IR (5%)                     : R$   {ir2} ')  
       print(f' (-) INSS ( 10%)                 : R$  {inss2} ')
       print(f' FGTS (11%)                      : R$  {fgts2} ')
       print(f' Total de descontos              : R$  {total_desc2} ')
       print(f' Salário Liquido                 : R$  {salario_liquid2} ')
elif salario >=1500 and salario<= 2500:    
       print(f'   Salário Bruto:                : R$ {salario} ')
       print(f' (-) IR (5%)                     : R$   {ir3} ')  
       print(f' (-) INSS ( 10%)                 : R$  {inss3} ')
       print(f' FGTS (11%)                      : R$  {fgts3} ')
       print(f' Total de descontos              : R$  {total_desc3} ')
       print(f' Salário Liquido                 : R$ {salario_liquid3} ')  
elif salario >= 2500:
       print(f' Salário Bruto:                  : R$ {salario} ')
       print(f' (-) IR (5%)                     : R$   {ir4} ')
       print(f' (-) INSS ( 10%)                 : R$  {inss4} ')
       print(f'  FGTS (11%)                     : R$  {fgts4} ')
       print(f'  Total de descontos             : R$  {total_desc4} ')
       print(f' Salário Liquido                 : R$ {salario_liquid4} ')       









