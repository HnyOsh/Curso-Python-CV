def leiaint(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print('\033[0;31mErro: por favor, digite um número inteiro válido.\033[m')
            continue
        except KeyboardInterrupt:
            print('\n\033[31mUsuário preferiu não digitar esse número..\033[m')
            return 0
        else:
            return n

def leiareal(msg):
    while True:
        try:
            n = float(input(msg))
        except (ValueError, TypeError):
            print('\033[0;31mErro: por favor, digite um número real válido.\033[m')
            continue
        except KeyboardInterrupt:
            print('\n\033[31mUsuário preferiu não digitar esse número..\033[m')
            return 0
        else:
            return n


# Example of usage
n1 = leiaint('Digite um Inteiro: ')
n2 = leiareal('Digite um Real: ')
print(f'O valor inteiro digitado foi {n1} e o real foi {n2}')
