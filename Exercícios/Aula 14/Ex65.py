escolha = 'S'
soma = totn = media = maiornum = menornum = 0

while escolha in 'Ss':
    num = int(input('Digite um valor: '))
    totn += 1
    soma += num

    if totn == 1:  # Inicializa maiornum e menornum com o primeiro número inserido
        maiornum = menornum = num
    else:
        if num > maiornum:
            maiornum = num
        if num < menornum:
            menornum = num

    escolha = input('Deseja continuar? [S/N] ').strip().upper()[0]

media = soma / totn

if totn > 0:
    print(f'Média dos valores digitados: {media}')
    print(f'Maior valor digitado: {maiornum}')
    print(f'Menor valor digitado: {menornum}')
else:
    print('Nenhum valor foi digitado.')
