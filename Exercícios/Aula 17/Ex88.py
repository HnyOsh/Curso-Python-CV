from random import randint
from time import sleep

megasena = []

print(f'-' * 40)
print(f'{"JOGA NA MEGA SENA":^40}')
print(f'-' * 40)

qntd = int(input('Quantos jogos você quer que eu sorteie ? '))
print(' ')

print(f'-=' * 6, f'SORTEANDO {qntd} JOGOS', f'-=' * 6)

for j in range(qntd):
    jogos = []
    while len(jogos) < 6:
        num = randint(0, 60)
        if num not in jogos:
            jogos.append(num)
    megasena.append(sorted(jogos))
    sleep(1)
    print(f'Jogo {j+1}: {sorted(jogos)}')

print(f'-=' * 7, f'< BOA SORTE! >', f'-=' * 7)
