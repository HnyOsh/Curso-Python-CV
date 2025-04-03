# Lista Composta
numeros = [[], []]

# Loop
for c in range(0, 7):
    num = int(input(f'Digite o {c+1}º valor: '))

    # Testando Par ou Ímpar
    if num % 2 == 0:
        numeros[0].append(num)
        numeros[0].sort()  # Colocando em ordem
    else:
        numeros[1].append(num)
        numeros[1].sort()  # Colocando em ordem

# Mostrando os resultados
print('-=' * 30)
print(f'Números pares: {numeros[0]}')
print(f'Números Ímpares: {numeros[1]}')
