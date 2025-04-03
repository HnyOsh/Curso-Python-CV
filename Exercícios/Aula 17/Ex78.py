valores = []

for cont in range(0, 5):
    valores.append(int(input(f'Digite um valor para a posição {cont}: ')))

maior_valor = max(valores)
menor_valor = min(valores)

print('=-' * 35)
print(f'Voce digitou os valores {valores}')

print(f'O maior valor digitado foi {maior_valor} nas posições ', end='')
for i, v in enumerate(valores):
    if v == maior_valor:
        print(f'{i}...', end='')
print()

print(f'O menor valor digitado foi {menor_valor} nas posições ', end='')
for i, v in enumerate(valores):
    if v == menor_valor:
        print(f'{i}...', end='')
print()
print('Cheguei ao final da lista.')
