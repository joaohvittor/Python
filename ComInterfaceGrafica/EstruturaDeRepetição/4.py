a =  80000
b =  200000
tempo = 0
while a < b:
    a = a + a*(0.03)
    b = b + b*(0.015)
    tempo = tempo + 1
else:
    print(a,b,tempo)