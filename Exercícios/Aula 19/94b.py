cadastro = {}
lista = []
soma = media = 0

while True:
    cadastro['Nome'] = str(input('Nome: ')).strip().capitalize()
    while True:
        cadastro['Sexo'] = str(input('Sexo? [M/F] ')).strip().upper()
        if cadastro['Sexo'] in 'MF':
            break
        print('Opção Inválida. Digite M ou F.')
    cadastro['Idade'] = int(input('Idade: '))
    soma += cadastro['Idade']

    lista.append(cadastro.copy())

    while True:
        continuar = str(input('Deseja continuar ? [S/N] ')).strip().upper()[0]
        if continuar in 'SN':
            break
        print('Erro! Digite S ou N.')
    if continuar == 'N':
        break

media = soma / len(lista)

print('-=' * 30)

print(f'A) Ao todo temos {len(lista)} pessoas cadastradas.')
print(f'B) A média de idade é de {media} anos. ')
print(f'C) As mulheres cadastradas foram ', end='')
for p in lista:
    if p['Sexo'] == 'F':
        print(f'{p["Nome"]}', end=' ')
print()
print(f'D) Lista das pessoas que estão acima da média: ')
for p in lista:
    if p['Idade'] >= media:
        print('    ', end='')
        for k, v in p.items():
            print(f'{k} = {v}; ', end='')
        print()

print('<< ENCERRADO >>')
