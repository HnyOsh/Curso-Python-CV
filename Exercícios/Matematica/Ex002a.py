# Ordem de precedência
# 1. () = Resolver tudo entre parentêses
# 2. ** = Potência
# 3. * / //- Divisão Inteira %- Resto da Divisão
# 4. + e -

n1 = int(input('Insira um número: '))
print('O seu número é {}, o número sucessor é {} e o número antecessor é {}.'.format(n1, (n1+1), (n1-1)))
