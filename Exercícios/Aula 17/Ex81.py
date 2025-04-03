valores = []
resp = 'S'
reverso = []

while resp == 'S':
    num = int(input('Digite um valor: '))
    valores.append(num)  # Adiciona o número diretamente, permitindo repetidos
    reverso = sorted(valores, reverse=True)

    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N] ')).strip().upper()
        if resp not in 'SN':
            print('Opção Incorreta!')

print('-=' * 20)
print(f'Você digitou {len(valores)} elementos.')  # Mostra a quantidade de números digitados
print(f'Os valores em ordem decrescente são {reverso}')

if 5 in valores:
    print(f'O valor 5 faz parte da lista e está na posição {reverso.index(5) + 1} na ordem decrescente.')
else:
    print('Não tem o valor 5 na lista!')
