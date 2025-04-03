from random import randint
from time import sleep
print('-=-' * 30)
print('Vou pensar em um número de 1 a 5. Tente adivinhar e ganhe um prêmio...')
print('-=-' * 30)
num = int(input('Em que número estou pensando ? '))
print('Processando . . .')
sleep(3)
resposta = randint(1, 5)
if num == resposta:
    print('\033[32mAcertou\033[m ! estava pensando no número {}, receba meus sinceros Parabéns como premiação.'.format(resposta))
else:
    print('\033[31mErrou\033[m, estava pensando no número {}, você terá que comprar algo pro Henry '
          'no Festival do Japão'.format(resposta))
