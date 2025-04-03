totn = s = 0

while True:
    n = int(input('Digite um número: '))
    if n == 999:
        break
    totn += 1
    s = s + n

print(f'A quantidade de números digitados foi {totn} e a soma entre eles foi {s}.')
