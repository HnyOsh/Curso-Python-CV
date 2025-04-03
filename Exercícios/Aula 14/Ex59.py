choice = -1

# Variaveis Globais
n1 = int(input('Digite o primeiro valor: '))
n2 = int(input('Digite o segundo valor: '))

# Opções
while choice != 5:
    # Menu
    print(' ')
    print('O que deseja fazer com esses valores ? ')
    print(' ')
    print('[1] Somar\n'
          '[2] Multiplicar\n'
          '[3] Maior\n'
          '[4] Novos Números\n'
          '[5] Sair do programa\n')
    choice = int(input('Digite uma opção: '))
    print(' ')

    if choice == 1:
        soma = n1 + n2
        print(f'A soma entre {n1} + {n2} é igual a {soma}')
        print(' ')
    elif choice == 2:
        multip = n1 * n2
        print(f'A multiplicação de {n1} * {n2} é igual a {multip} ')
        print(' ')
    elif choice == 3:
        if n1 > n2:
            maior = n1
        else:
            maior = n2
        print(f'O maior valor digitado foi {maior}')
        print(' ')
    elif choice == 4:
        print('Resetando os números...')
        n1 = int(input('Digite o primeiro valor: '))  # Mudando as variaveis
        n2 = int(input('Digite o segundo valor: '))  # Mudando as variaveis
    elif choice != 5:
        print('Opção Inválida !')
        print('Tente Novamente')
        print(' ')

# Fim de Programa
print('Saindo...')
