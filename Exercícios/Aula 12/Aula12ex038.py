n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))
if n1 > n2:
    print('\033[1mO primeiro número\033[m é maior que o segundo')
elif n2 > n1:
    print('\033[1mO segundo número\033[m é maior que o primeiro')
else:
    print('\033[1mNão existe maior número\033[m, os dois valores são iguais !')
