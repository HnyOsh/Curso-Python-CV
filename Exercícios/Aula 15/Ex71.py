# Introdução
print('=' * 40)
print(f'{"BANCO CEV":^40}')
print('=' * 40)
print(' ')

saque = int(input('Que valor você deseja sacar ? R$'))

cedula_atual = 50

while True:
    cedulas = saque // cedula_atual
    saque = saque % cedula_atual

    if cedulas > 0:
        print(f'Total de {cedulas} cédulas de R${cedula_atual}.')

    if cedula_atual == 50:
        cedula_atual = 20
    elif cedula_atual == 20:
        cedula_atual = 10
    elif cedula_atual == 10:
        cedula_atual = 1
    else:
        break

print(' ')
print('Operação Finalizada')
