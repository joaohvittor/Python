arquivo = float(input('por favor insira o tamanho do arquivo para download em MB: \n'))
speed_net = float(input('por favor insira a velocidade do link em Mbps: \n'))
tempo = arquivo/speed_net
minutos = tempo/60
print(f'Seu arquivo de {arquivo} MB levará {minutos} minutos para completar o download. \n')