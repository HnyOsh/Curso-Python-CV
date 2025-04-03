from time import sleep


def contador(i, f, p):
    if p < 0:
        p *= -1
    if p == 0:
        p = 1

    print('-=' * 20)
    print(f'Contagem de {i} até {f} de {abs(p)} em {abs(p)}')
    sleep(2.5)

    if i < f:
        c = i
        while c <= f:
            print(f'{c} ', end='', flush=True)
            sleep(0.5)
            c += p
        print('FIM!')
    else:
        c = i
        while c >= f:
            print(f'{c} ', end='', flush=True)
            sleep(0.5)
            c -= p
        print('FIM!')


contador(1, 10, 1)
contador(10, 0, 2)

print('-=' * 20)
print('Agora é sua vez de personalizar a contagem!')
ini = int(input('Início: '))
fim = int(input('Fim:    '))
pas = int(input('Passo:  '))
contador(ini, fim, pas)
