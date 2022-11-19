nota1 = float(input("insira a primeira nota do aluno: \n"))
nota2 = float(input("insira a segunda nota do aluno: \n"))
media = (nota1+nota2)/2
if media >= 9 and media <= 10.0:
    print('Média de Aproveitamento  Conceito \n')
    print('Entre 9.0 e 10.0           A')
    print('APROVADO')
elif media >= 7.5 and media <= 9.0:
    print('Média de Aproveitamento  Conceito \n')   
    print('Entre 7.5 e 9.0            B')
    print('APROVADO')
elif media >= 6 and media <= 7.5:
    print('Média de Aproveitamento  Conceito')    
    print('Entre 6.0 e 7.5           C')
    print('APROVADO')
elif media >= 4.0 and media <= 6.0:
    print('Média de Aproveitamento  Conceito \n')   
    print('Entre 4.0 e 6.0            D')
    print('REPROVADO')
elif media >= 4.0 and media <= 0:
    print('Média de Aproveitamento  Conceito')    
    print('Entre 4.0 e zero           E')
    print('REPROVADO')




