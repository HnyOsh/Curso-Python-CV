# Ordem de precedência
# 1. () = Resolver tudo entre parentêses
# 2. ** = Potência
# 3. * / //- Divisão Inteira %- Resto da Divisão
# 4. + e -

celsius = float(input('Informe a temperatura em ºC: '))
far = ((9*celsius)/5) + 32
kel = celsius + 273.15
print('-' * 50)
print('A temperatura de {:.1f}ºC corresponde a {:.1f}ºF e {:.1f}K.'.format(celsius, far, kel))
