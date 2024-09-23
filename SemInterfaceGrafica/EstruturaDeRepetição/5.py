a =  80000
b =  200000
c = float(input('Insira a taxa de crescimento'))
tempo = 0
while a < b:
    a = a + a*c
    b = b + b*c
    tempo = tempo + 1
else:
    print(f'{a} {b} {tempo}')