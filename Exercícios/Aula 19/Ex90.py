aluno = {}
cadastro = []

aluno['Nome'] = str(input('Nome: '))
aluno['Média'] = float(input(f'Média de {aluno["Nome"]}: '))
if aluno['Média'] >= 7:
    aluno['Situação'] = 'Aprovado'
else:
    aluno['Situação'] = 'Reprovado'
cadastro.append(aluno.copy())

for k, v in aluno.items():
    print(f'{k} é igual a {v}')
