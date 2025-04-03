from datetime import datetime
ano_atual = datetime.now().year
nascimento = int(input('Digite o ano do seu nascimento para saber sua categoria na natação: '))
idade = ano_atual - nascimento
if idade <= 9:
    print('Você tem {} anos, portanto é da categoria Mirim !'.format(idade))
elif idade <= 14:
    print('Voce tem {} anos, portanto é da categoria Infantil !'.format(idade))
elif idade <= 19:
    print('Você tem {} anos, portanto é da categoria Junior !'.format(idade))
elif idade <= 25:
    print('Você tem {} anos, portanto é da categoria Sênior !'.format(idade))
else:
    print('Você tem {} anos, portanto é da categoria Master !'.format(idade))
