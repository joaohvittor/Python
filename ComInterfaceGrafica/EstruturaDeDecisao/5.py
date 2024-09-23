nota1 = float(input('Insira a primeira nota do aluno: \n'))
nota2 = float(input('Insira a segunda nota do aluno: \n'))
media = (nota1 + nota2) / 2

if media == 10:
    print('Aprovado com distinção')
elif media >= 7:
    print('Aprovado')    
else:
    print('Reprovado')
