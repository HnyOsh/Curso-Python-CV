# Ordem de precedência
# 1. () = Resolver tudo entre parentêses
# 2. ** = Potência
# 3. * / //- Divisão Inteira %- Resto da Divisão
# 4. + e -

print('Coloque o valor do produto e descubra o valor do desconto à vista ou valor parcelado')
valor = float(input('Preço: R$'))
print('-' * 20)
print('Coloque a porcentagem de desconto para o cliente')
desconto = float(input('Desconto: %'))
print('-' * 20)
print('Coloque a porcentagem de juros se o produto for parcelado')
parcelado = float(input('Parcelado: %'))
print('-' * 20)
vdesc = valor - (valor * desconto / 100)
vparc = valor + (valor * parcelado / 100)
print('Valor Original: R${:.2f} '
      '\nValor com Desconto de {:.2f}%: R${:.2f} '
      '\nValor Parcelado com juros de {:.2f}%: R${:.2f}'
      .format(valor, desconto, vdesc, parcelado, vparc))
print('-' * 20)
