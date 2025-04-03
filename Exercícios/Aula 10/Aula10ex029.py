km = float(input('Digite a velocidade que passou no radar para saber se foi multado: '))
e = km - 80
m = float(km - 80) * 7
if km >= 80:
    print('Você estava \033[1;31;97m{}KM/H\033[m acima do permitido, que é 80Km/h, portanto será multado no valor de R${:.2f} '.format(e, m))
else:
    print('Você estava dentro do limite de velocidade da pista. Continue assim !')
