def area(lar, com):
    terreno = lar * com
    print(f'A área de um terreno {lar} x {com} é de {terreno}m²')


print('Controle de Terrenos')
print('-' * 15)
l = float(input('LARGURA (m): '))
c = float(input('COMPRIMENTO (m): '))
area(l, c)
