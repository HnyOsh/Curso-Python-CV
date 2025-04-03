from time import sleep
from random import randint


def sorteia():
    print('Sorteando 5 valores da lista: ', end='')
    for c in range(0, 5):
        num = randint(0, 10)
        numeros.append(num)
        sleep(0.3)
        print(num, end=' ', flush=True)
    print('PRONTO !')


def somapar():
    soma = 0
    for v in numeros:
        if v % 2 == 0:
            soma += v
    print(f'Somando os valores pares de {numeros}, temos {soma}')


numeros = []

sorteia()
somapar()
