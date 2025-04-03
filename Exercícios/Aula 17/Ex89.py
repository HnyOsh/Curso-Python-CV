alunos = []
continuar = 'S'

while continuar == 'S':
    nome = str(input('Nome: '))
    n1 = float(input('Nota 1: '))
    n2 = float(input('Nota 2: '))
    media = (n1 + n2) / 2
    alunos.append([nome, [n1, n2], media])

    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Deseja continuar? [S/N] ')).strip().upper()
        if continuar not in 'SN':
            print('Opção Inválida! Digite S ou N.')

print('-=' * 15)
print(f'{"No.":3}', f'{"NOME":15}', f'{"MÉDIA":>6}')
print('-=' * 15)

for i, aluno in enumerate(alunos):
    print(f'{i:<4}{aluno[0]:<15}{aluno[2]:>6.1f}')

print('-' * 40)

while True:
    opcao = int(input('Mostrar notas de qual aluno ? (999 interrompe): '))
    if opcao == 999:
        break
    if opcao <= len(alunos) - 1:
        print(f'Notas de {alunos[opcao][0]} são {alunos[opcao][1]}')
