n1 = float(input('Nota da primeira prova: '))
n2 = float(input('Nota da segunda prova: '))
media = (n1 + n2) / 2
if media < 5:
    print('Você foi reprovado por {:.1f} pontos, sua media foi {:.1f}'.format(7 - media, media))
elif 7 > media >= 5:
    print('Voce está de recuperação por {:.1f} pontos, sua media foi {:.1f}'.format(7 - media, media))
elif media >= 7:
    print('Voce foi aprovado, sua média de notas é {:.1f}. PARABENS !'.format(media))
