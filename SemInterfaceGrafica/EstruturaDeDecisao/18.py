dia = int(input('Insira o dia referente a data a ser consultada: \n'))
mes = int(input('Insira o mês referente a data a ser consultada: \n'))
ano = int(input('Insira o ano referente a data a ser consultada: \n'))
if dia <=31 and mes <=12:
    print(f'{dia}/{mes}/{ano}')
else:
    print('Formato inválido')    