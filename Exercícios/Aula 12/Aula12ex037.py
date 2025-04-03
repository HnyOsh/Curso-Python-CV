# Condições de conversão
print(' ')
num = int(input('Digite um número: '))
print('Escolha uma das bases para conversão:')
print(' ')
print('[1] para Binário\n[2] para Octal\n[3] para Hexadecimal:')
print(' ')
escolha = int(input('Sua opção: '))

# Conversões
if escolha == 1:
    binario = bin(num)[2:]
    print('A conversão do número {} em binário é {}'.format(num, binario))
elif escolha == 2:
    octal = oct(num)[2:]
    print('A conversão do número {} em octal é {}'.format(num, octal))
elif escolha == 3:
    hexa = hex(num)[2:]
    print('A conversão do número {} em hexadecimal é {}'.format(num, hexa))
elif escolha != 1 or 2 or 3:
    print('Opção Invalida !')
    