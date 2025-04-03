'''from random import shuffle

grupo1 = input('Primeiro Grupo: ')
grupo2 = input('Segundo Grupo: ')
grupo3 = input('Terceiro Grupo: ')
grupo4 = input('Quarto Grupo: ')

lista = [grupo1, grupo2, grupo3, grupo4]

shuffle(lista)

print('A ordem de apresentação do grupo de trabalhos será: ')
for i, grupo in enumerate(lista, start=1):
    print(f'{i}. {grupo}')'''

from random import shuffle
print('Digite os nomes dos alunos para ver a ordem das apresentações do trabalho.')
a1 = str(input('Aluno 1: '))
a2 = str(input('Aluno 2: '))
a3 = str(input('Aluno 3: '))
a4 = str(input('Aluno 4: '))
lista = [a1, a2, a3, a4]
shuffle(lista)
print('-' * 80)
print('A ordem das apresentações do trabalho será: ')
print(lista)
