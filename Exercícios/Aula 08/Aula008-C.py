'''from random import sample
a1 = str(input('Aluno 1: '))
a2 = str(input('Aluno 2: '))
a3 = str(input('Aluno 3: '))
a4 = str(input('Aluno 4: '))
esc = [a1, a2, a3, a4]
print('O aluno escolhido foi {}'.format(sample(esc, 1)))'''

import random
print('Quem vai escolher o próximo filme ? ')
print('-' * 80)
a1 = str(input('Nome 1: '))
a2 = str(input('Nome 2: '))
lista = [a1, a2]
escolhido = random.choice(lista)
print('-' * 80)
print('A pessoa que vai escolher o proximo filme é {}'.format(escolhido))
print('Parabéns !')
print('-' * 80)
print('-' * 80)
print('OBS: A pessoa não selecionada não poderá reclamar do filme escolhido e nem dormir no meio')
print('OBS2: FILME DE HEROIS LIBERADOS')
print('Te amo')
