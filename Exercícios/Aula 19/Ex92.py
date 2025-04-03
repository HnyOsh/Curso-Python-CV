from datetime import datetime

ano_atual = datetime.now().year

dic = {}
lista = []

dic['Nome'] = str(input('Nome: '))
nascimento = int(input('Ano de Nascimento: '))
dic['Idade'] = ano_atual - nascimento
dic['CTPS'] = int(input('Carteira de Trabalho (0 não tem): '))

if dic['CTPS'] != 0:
    dic['Contratação'] = int(input('Ano da contratação: '))
    dic['Salário'] = float(input('Salário: '))
    dic['Aposentadoria'] = dic['Idade'] + ((dic['Contratação'] + 35) - ano_atual)

lista.append(dic.copy())

print('-=' * 30)
for c in lista:
    for k, v in c.items():
        print(f'   - {k} tem o valor {v}')
