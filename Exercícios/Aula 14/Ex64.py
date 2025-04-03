'''num = totn = soma = 0

while num != 999:
    num = int(input('Digite um valor [999 para Parar]: '))
    if num != 999:
        totn = totn + 1
        soma = soma + num

print('Fim do Programa')
print(f'Quantidade de números digitados: {totn}')
print(f'A soma de todos os valores digitados: {soma}')'''

num = totn = soma = 0
num = int(input('Digite um valor [999 para Parar]: '))

while num != 999:
    totn = totn + 1
    soma = soma + num
    num = int(input('Digite um valor [999 para Parar]: '))

print('Fim do Programa')
print(f'Quantidade de números digitados: {totn}')
print(f'A soma de todos os valores digitados: {soma}')
