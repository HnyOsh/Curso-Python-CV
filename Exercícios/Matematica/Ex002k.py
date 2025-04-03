# Ordem de precedência
# 1. () = Resolver tudo entre parentêses
# 2. ** = Potência
# 3. * / //- Divisão Inteira %- Resto da Divisão
# 4. + e -

d = int(input('Quantos dias alugados? '))
km = float(input('Quantos Km rodados? '))
preco = (d * 60) + (km * 0.15)
print('-' * 30)
print('O total a pagar é de R${:.2f}'.format(preco))
