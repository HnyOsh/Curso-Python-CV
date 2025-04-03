import random
from time import sleep

# Opções do jogo
opcoes = ['pedra', 'papel', 'tesoura']

# Escolha do jogador
print(' ')
print('Escolha pedra, papel ou tesoura: ')
print(' ')
jogador = str(input('Qual é a sua escolha? ').lower()).strip()
print(' ')

# Verificar se a escolha do jogador é válida
if jogador == 'pedra' or jogador == 'papel' or jogador == 'tesoura':
    # Escolha do computador
    computador = random.choice(opcoes)

    # Apresentação
    sleep(1)
    print('Jô')
    sleep(1)
    print('Ken')
    sleep(1)
    print('Po')
    sleep(2)
    print(' ')

    # Determinando o vencedor
    if jogador == computador:
        print('Empate!')
    elif jogador == 'pedra':
        if computador == 'tesoura':
            print('Você ganhou! Pedra quebra tesoura.')
        else:
            print('Você perdeu! Papel cobre pedra.')
    elif jogador == 'papel':
        if computador == 'pedra':
            print('Você ganhou! Papel cobre pedra.')
        else:
            print('Você perdeu! Tesoura corta papel.')
    elif jogador == 'tesoura':
        if computador == 'papel':
            print('Você ganhou! Tesoura corta papel.')
        else:
            print('Você perdeu! Pedra quebra tesoura.')
else:
    print('Escolha inválida! Tente novamente.')

print(' ')
print('O computador escolheu: {}'.format(computador))
print(' ')
