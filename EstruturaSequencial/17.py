metrosquad = float(input('Por favor insira a quantidade de metros quadrados: \n'))
preço_lata = (80*metrosquad)/18
preço_galão = (80*metrosquad)/3.6
cobertura = metrosquad/6
qntd_lata = (cobertura*6)/18
qntd_galão = (cobertura*6)/3.6
mistura_lata = float(qntd_lata / 18.0)
mistura_galao = float((qntd_galão - (mistura_lata * 18)) / 3.6)
print(f'Voçê precisará de {qntd_lata} latas de tinta com o preço total de R${preço_lata} \n')
print(f'Voçê precisará de {qntd_galão} galões  de tinta com o preço total de R${preço_galão} \n')
print(f'Em caso de mistura serão {mistura_lata} latas e {mistura_galao} galões  ')

 