n = 1
totp = 0
toti = 0

while n != 0:
    n = int(input('Digite um valor: '))
    if n != 0:
        if n % 2 == 0:
            totp = totp + 1
        if n % 2 == 1:
            toti = toti + 1

print(f"O Total de números pares digitados foram {totp}")
print(f'O Total de números ímpares digitados foram {toti}')
