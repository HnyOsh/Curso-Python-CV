# Ordem de precedência
# 1. () = Resolver tudo entre parentêses
# 2. ** = Potência
# 3. * / //- Divisão Inteira %- Resto da Divisão
# 4. + e -
# obs: Raiz Quadrada **(1/2)

nt1 = float(input('Insira a nota da primeira prova: '))
nt2 = float(input('Insira a nota da segunda prova: '))
m = (nt1 + nt2) / 2
print('A nota da sua primeira prova foi {}, da segunda prova foi {}. \nA sua média de notas é {}'.format(nt1, nt2, m))
