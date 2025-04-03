from time import sleep


def exibir_mensagem(msg, cor, sleep_time=0):
    largura = len(msg) + 4
    print(f'\033[{cor}m' + '~' * largura)
    print(f'  {msg}  ')
    print('~' * largura)
    print('\033[m')  # Reseta as cores
    if sleep_time:
        sleep(sleep_time)


def manual(comando):
    print('\033[47m')  # Fundo branco
    help(comando)
    print('\033[m')  # Reseta as cores


# Loop principal
while True:
    exibir_mensagem('SISTEMA DE AJUDA PyHELP', '42')  # Verde
    opc = input('Função ou Biblioteca > ').strip().lower()
    if opc == 'sair':
        break
    print()
    exibir_mensagem(f'Acessando o manual do comando {opc}', '44', 2)  # Azul
    manual(opc)
    sleep(4)

print('')
exibir_mensagem('ATÉ LOGO!', '41')  # Vermelho
