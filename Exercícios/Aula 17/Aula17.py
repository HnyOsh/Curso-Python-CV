'''num = [2, 5, 9, 1]
num[2] = 3
num.append(7)
num.sort(reverse=True)
num.insert(2, 2)
num.remove(2)  #procura a primeira ocorrencia

if 5 in num:
    num.remove(5)
else:
    print('Não achei o número 5')

#num.pop(2)

print(num)
print(f'Essa lista tem {len(num)} elementos.')'''

valores = list()
for cont in range(0,5):
    valores.append(int(input('Digite um valor: ')))

for c, v in enumerate(valores):
    print(f'Na posição {c} encontrei o valor {v}...')
print('Cheguei ao final da lista.')
