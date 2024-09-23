a = float(input('Insira o valor para a : \n'))
b = float(input('Insira o valor para b : \n'))
c = float(input('Insira o valor para c : \n'))
delta = b**2 - (4*a*c)
raizdel = float(delta) ** 0.5
x = -b + raizdel
if (a==0):
    print('Numero invalido')
elif (a > 0) :
    if delta < 0:
        print('Raizes imaginarias')   
    elif delta == 0:
        raiz = -b / (2*a)
        print(f'Delta = 0, raiz = {raiz}')
    else:
        raiz1 = (-b + raiz) / (2*a)    
        raiz2 = (-b - raiz) / (2*a)
        print(f'Raizes = {raiz1}{raiz2}')
else:
    print('Formato invalido')        
            






##
##if(a==0):
##     print('Se a=0, não é equação do segundo grau. Tchau')
##elif (a >= 0):
##   if delta<0:
##     print('Delta menor que 0. Raízes imaginárias. Tchau')
##   elif delta==0:
##     raiz = -b / (2*a)
##     print('Delta=0 , raiz = ',raiz)
##else:
##  raiz1 = (-b + raiz ) / (2*a)
##  raiz2 = (-b - raiz ) / (2*a)
##print(f'Raizes: {raiz1} e {raiz2}')