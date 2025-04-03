times = []

while True:

    jogador = {}
    partidas = []

    jogador['Nome'] = str(input('Nome do Jogador: ')).capitalize().strip()
    tot = int(input(f'Quantas partidas {jogador["Nome"]} jogou ? '))

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

print(f'{"cod":<4}', f'{"Nome":<15}', f'{"Gols":<15}', f'{"Total":>6}')
for i, jog in enumerate(times):
    print(f'{i + 1:<4}', f'{jog["Nome"]:<15}', f'{str(jog["Gols"]):<15}', f'{jog["Total"]:>6}')
print('-=' * 30)

while True:
    mostrar = int(input('Mostrar dados de qual jogador ? (999 para parar) '))
    for i, jog in enumerate(times):
        if mostrar == i + 1:
            print(f' -- LEVANTAMENTO DO JOGADOR {jog["Nome"]}:')
            for c, gols in enumerate(jogador["Gols"]):
                print(f'    No jogo {c + 1} fez {gols} gols')
    if mostrar == 999:
        break
print('Programa Encerrado')