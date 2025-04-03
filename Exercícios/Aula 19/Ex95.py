times = []
jogador = {}
partidas = []

while True:
    jogador.clear()
    jogador['Nome'] = str(input('Nome do Jogador: ')).capitalize().strip()
    tot = int(input(f'Quantas partidas {jogador["Nome"]} jogou ? '))
    partidas.clear()
    for c in range(tot):
        partidas.append(int(input(f'   Quantos gols na partidas {c + 1}? ')))
    print('-=' * 30)

    jogador['Gols'] = partidas[:]
    jogador['Total'] = sum(partidas)
    times.append(jogador.copy())

    while True:
        continuar = str(input('Quer continuar ? [S/N] ')).strip().upper()
        if continuar in 'SN':
            break
    if continuar == 'N':
        break
print('-=' * 30)

print('cod ', end='')
for i in jogador.keys():
    print(f'{i:<15}', end='')
print()
print('-=' * 30)
for k, v in enumerate(times):
    print(f'{k:>3} ', end='')
    for d in v.values():
        print(f'{str(d):<15}', end='')
    print()
print('-=' * 30)

while True:
    mostrar = int(input('Mostrar dados de qual jogador ? (999 para parar) '))
    if mostrar == 999:
        break
    if mostrar >= len(times):
        print(f'Erro! Não existe jogador com código {mostrar}!')
    else:
        print(f' -- LEVANTAMENTO DO JOGADOR {times[mostrar]["Nome"]}:')
        for c, gols in enumerate(times[mostrar]["Gols"]):
            print(f'    No jogo {c + 1} fez {gols} gols')
print('')
print('Programa Encerrado')
