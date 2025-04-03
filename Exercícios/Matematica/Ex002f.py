# Ordem de precedência
# 1. () = Resolver tudo entre parentêses
# 2. ** = Potência
# 3. * / //- Divisão Inteira %- Resto da Divisão
# 4. + e -

larg = float(input('Largura da parede: '))
altu = float(input('Altura da parede: '))
mc = larg * altu
t = mc / 2
print('Sua parede tem a dimensão de {:.2f}x{:.2f} e sua área é de {:.2f}m².'.format(larg, altu, mc))
print('Para pintar essa parede, você precisará de {:.2f}l de tinta.'.format(t))
