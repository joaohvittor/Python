letra = str(input('Insira uma letra: \n')).lower()
if letra in ["a", "e", "i", "o", "u"]:
    print('Vogal')
else:
    print('Você digitou uma consoante')
