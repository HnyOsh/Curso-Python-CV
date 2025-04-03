# Ordem de precedência
# 1. () = Resolver tudo entre parentêses
# 2. ** = Potência
# 3. * / //- Divisão Inteira %- Resto da Divisão
# 4. + e -
# obs: Raiz Quadrada **(1/2)

n1 = int(input('Insira um número: '))
# dobro = n1 * 2
# triplo = n1 * 3
# rq = n1 ** (1/2)
print('O seu número é {} \n'
      'O dobro dele é {} \n'
      'O triplo é {} \n'
      'E a raiz quadrada é {:.2f}.'.format(n1, (n1 * 2), (n1 * 3), pow(n1, 1 / 2)))
# 'E a raiz quadrada é {:.2f}.'.format(n1, (n1 * 2), (n1 * 3), (n1 ** (1/2))))
