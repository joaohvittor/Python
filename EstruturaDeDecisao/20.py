nota1 = float(input('Insira a primeiro nota do aluno: \n'))
nota2 = float(input('Insira a segunda nota do aluno: \n'))
nota3 = float(input('Insira a terceira nota do aluno: \n'))
media = (nota1+nota2+nota3)/3
if media >= 10:
    print('Aprovado com distinção')
elif media >= 7 and media <= 9:
    print('Aprovado')    
else:
    print('Reprovado')    