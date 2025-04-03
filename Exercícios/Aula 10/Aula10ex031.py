km = float(input('Digite a distância que percorrera para calcular o valor da passagem: '))
if km <= 200:
    print('Você percorrera {}Km, portanto o valor da sua passagem é R${:.2f}'.format(km, km * 0.50))
else:
    print('Voce percorrera {}Km, portanto o valor da sua passagem é R${:.2f}'.format(km, km * 0.45))
