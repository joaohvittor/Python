lado1 = float(input('insira o valor primeiro do lado do triangulo: \n'))
lado2 = float(input('insira o valor do segundo lado do triangulo: \n'))
lado3 = float(input('insira o valor do terceiro lado do triangulo: \n'))
if lado1 != lado2 and lado1 != lado3:
    print('Triangulo escaleno')
elif lado1 == lado2 and lado1 ==lado3:
    print('Triangulo Equilatero')   
elif lado1 == lado2 or lado2 == lado3 or lado1 == lado3:
    print('Triangulo isoceles')     
