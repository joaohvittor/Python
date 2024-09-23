produto1 = str(input('Insira o nome do primeiro produto: \n'))
preço_produto1 = float(input('Insira o preço do primeiro produto: \n'))
produto2 = str(input('Insira o nome do segundo produto: \n'))
preço_produto2 = float(input('Insira o preço do segundo produto: \n'))
produto3 = str(input('Insira o nome do terceiro produto: \n'))
preço_produto3 = float(input('Insira o preço do terceiro produto: \n'))
if preço_produto1<preço_produto2 and preço_produto1<preço_produto3:
    print(f'Voçê deve comprar o produto {produto1} que custa R${preço_produto1} por ser mais barato que os produtos {produto2} e {produto3}')
elif preço_produto2<preço_produto1 and preço_produto2<preço_produto3:
    print(f'Voçê deve comprar o produto {produto2} que custa R${preço_produto2} por ser mais barato que os produtos {produto1} e {produto3}')
elif preço_produto3<preço_produto2 and preço_produto3<preço_produto1:
    print(f'Voçê deve comprar o produto {produto3} que custa R${preço_produto3} por ser mais barato que os produtos {produto3} e {produto2}')
