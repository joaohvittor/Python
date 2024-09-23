metrosquad = float(input('Por favor insira a quantidade de metros quadrados: \n'))
preço_lata = (80*metrosquad)/18
cobertura = metrosquad/3
qntd_lata = (cobertura*3)/18
print(f'Voçê precisará de {qntd_lata} latas de tinta com o preço total de R${preço_lata} \n')

