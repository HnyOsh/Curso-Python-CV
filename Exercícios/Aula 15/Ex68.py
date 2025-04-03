from random import randint

cont = 0

while True:
    # Introdução
    largura = 40
    texto = 'VAMOS JOGAR PAR OU ÍMPAR'
    espacos = (largura - len(texto)) // 2

    print('=-' * 20)
    print(' ' * espacos + texto)
    print('=-' * 20)

    n = int(input('Digite um valor: '))
    computador = randint(0, 10)
    soma = computador + n

    escolha = ' '
    while escolha not in 'PI':
        escolha = str(input('Par ou Ímpar? [P/I] ')).strip().upper()[0]
    print('=-' * 20)

    print(f'Você jogou {n} e computador {computador}. Total de {soma}')
    print('DEU PAR' if soma % 2 == 0 else 'DEU IMPAR', end='')
    print(' ')

    # Escolha Par
    if escolha == 'P':
        if soma % 2 == 0:
            print('=-' * 20)
            print('Você VENCEU!')
            cont += 1
        else:
            print('=-' * 20)
            print('Você PERDEU!')
            break

    # Escolha Ímpar
    elif escolha == 'I':
        if soma % 2 == 1:
            print('=-' * 20)
            print('Você VENCEU!')
            cont += 1
        else:
            print('=-' * 20)
            print('Você PERDEU!')
            break

    print('Vamos jogar Novamente...')
    print(' ')
print(f'GAME OVER... Você venceu {cont} vezes.')
