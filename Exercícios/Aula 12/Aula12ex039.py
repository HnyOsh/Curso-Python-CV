from datetime import datetime
ano_atual = datetime.now().year
nascimento = int(input('Digite o ano de nascimento para ver quanto tempo falta para se alistar: '))
idade = ano_atual - nascimento
if idade < 18:
    print('Você ainda tem que esperar {} ano(s) para se alistar ao serviços militar.'.format(18 - idade))
elif idade == 18:
    print('Você ja pode se alistar !')
else:
    print('Você passou {} ano(s) do periodo de alistamento do serviço militar.'.format(idade - 18))
