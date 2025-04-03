valores = []
resp = 'S'
vp = []
vi = []

while resp == 'S':
    num = int(input('Digite um número: '))
    valores.append(num)
    if num % 2 == 0:
        vp.append(num)
    else:
        vi.append(num)

    resp = ' '
    while resp not in 'SN':
        resp = (str(input('Quer continuar ? [S/N] '))).strip().upper()
        if resp not in 'SN':
            print('Opção Inválida !')

print('-=' * 30)
print(f'A lista completa é {valores}')
print(f'A lista de pares é {vp}')
print(f'A lista de ímpares é {vi}')
