dic = {}
lista = []  # Lista para armazenar os dicionários
contp = 0  # Contador de pessoas

while True:
    dic['Nome'] = str(input('Nome: ')).strip().capitalize()
    while True:
        dic['Sexo'] = str(input('Sexo: [M/F] ')).strip().upper()
        if dic['Sexo'] in 'MF':
            break
        print('ERRO! Por favor, digite apenas M ou F.')
    dic['Idade'] = int(input('Idade: '))
    contp += 1
    lista.append(dic.copy())  # Copia o dicionário para a lista

    while True:
        pergunta = str(input('Quer continuar? [S/N] ')).strip().upper()
        if pergunta in 'SN':
            break
        print('Erro! Responda apenas com S ou N.')
    if pergunta == "N":
        break

# Calculando a média de idade
media = sum(pessoa['Idade'] for pessoa in lista) / contp
print('-=' * 25)

# Exibindo o total de pessoas
print(f'- O grupo tem {contp} pessoas.')
print(f'- A média de idade é de {media:.2f} anos.')

# Exibindo as mulheres cadastradas
print(f'- As mulheres cadastradas foram: ', end='')
mulheres = [pessoa['Nome'] for pessoa in lista if pessoa['Sexo'] == 'F']

if mulheres:
    print(', '.join(mulheres))
else:
    print('Nenhuma mulher foi cadastrada.')

# Exibindo pessoas com idade acima da média
print('- Lista de pessoas com idade acima da média:')
for pessoa in lista:
    if pessoa['Idade'] > media:
        print(f"  {pessoa['Nome']} do sexo {pessoa['Sexo']} com {pessoa['Idade']} anos.")
