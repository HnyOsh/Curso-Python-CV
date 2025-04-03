numero = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze',
          'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')

while True:
    entrada_valida = False
    while not entrada_valida:
        escolha_str = input('Digite um número entre 0 e 20: ')
        if escolha_str.isdigit():  # Verifica se a entrada é um número
            escolha = int(escolha_str)
            if 0 <= escolha <= 20:
                entrada_valida = True
                print(f'Você digitou o número {numero[escolha]}')
            else:
                print('Número inválido! Tente novamente.')
        else:
            print('Entrada inválida! Por favor, digite um número.')

    continuar = input('Você quer continuar? [S/N] ').strip().upper()

    while continuar not in 'SN':
        print('Opção inválida! Digite S para Sim ou N para Não.')
        continuar = input('Você quer continuar? [S/N] ').strip().upper()

    if continuar == 'N':
        print('Programa encerrado.')
        break