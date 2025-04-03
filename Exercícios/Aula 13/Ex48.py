s = 0
for c in range(0, 501):
    if c % 2 == 1 and c % 3 == 0:
        s = s + c
print(f'A soma de todos os números impares é {s}')
