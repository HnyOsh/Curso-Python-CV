tot18 = toth = totmul = 0
continuar = 'S'

while continuar == 'S':

    # Introdução
    largura = 40
    texto = 'CADASTRE UMA PESSOA'
    espacos = (largura - len(texto)) // 2

    print('-' * 40)
    print(' ' * espacos + texto)
    print('-' * 40)

    while True:
        idade = int(input('Idade: '))
        if idade >= 0:
            break  # Sai do loop se a idade for válida
        else:
            print("A idade não pode ser negativa. Tente novamente.")

    # Validação do sexo
    while True:
        sexo = str(input('Sexo: [M/F]  ')).strip().upper()
        if sexo in ['M', 'F']:
            break
        else:
            print("Entrada inválida. Por favor, digite 'M' para masculino ou 'F' para feminino.")

    if idade >= 18:
        tot18 += 1  # Conta apenas se a idade for 18 ou mais
    if sexo == 'M':
        toth += 1
    if sexo == 'F' and idade < 20:
        totmul += 1

    print('-' * 40)

    # Validação da continuidade
    while True:
        continuar = str(input('Deseja continuar ? [S/N] ')).strip().upper()
        if continuar in ['S', 'N']:
            break
        else:
            print("Entrada inválida. Por favor, digite 'S' para continuar ou 'N' para sair.")

    print(' ')

print('=' * 12, 'FIM DO PROGRAMA', '=' * 12)
print(f'Total de pessoas com mais de 18 anos: {tot18}')
print(f'Ao todo temos {toth} homens cadastrados.')
print(f'E temos {totmul} mulheres com menos de 20 anos.')
