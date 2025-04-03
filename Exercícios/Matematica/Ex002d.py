# Ordem de precedência
# 1. () = Resolver tudo entre parentêses
# 2. ** = Potência
# 3. * / //- Divisão Inteira %- Resto da Divisão
# 4. + e -

reais = float(input('Valor em R$: '))
dol = reais / 3.27
print('O valor convertido em dollares é ${:.2f}'.format(dol))
#print('O valor convertido em dollares é US${:.2f}'.format(reais / 3.27))
