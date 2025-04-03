jogador = {}
partidas = []

jogador['Nome'] = str(input('Nome do Jogador: ')).capitalize().strip()
tot = int(input(f'Quantas partidas {jogador["Nome"]} jogou ? '))

for c in range(tot):
    partidas.append(int(input(f'   Quantos gols na partidas {c + 1}? ')))
print('-=' * 30)

jogador['Gols'] = partidas[:]
jogador['Total'] = sum(partidas)

for k, v in jogador.items():
    print(f'O campo {k} tem o valor {v}')
print('-=' * 30)

print(f'O jogador {jogador["Nome"]} jogou {len(partidas)} partidas.')
for i, v in enumerate(partidas):
    print(f'   => Na partida {i + 1}, fez {v} gols.')
print(f'Foi um total de {jogador["Total"]} gols.')
