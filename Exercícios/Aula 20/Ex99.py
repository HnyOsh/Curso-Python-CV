from time import sleep


def maior(*num):
    totn = 0
    print('-=' * 20)
    print('Analisando os valores passados...')
    if len(num) > 0:
        for v in num:
            totn += 1
            sleep(0.5)
            print(v, end=' ', flush=True)
        print(f'Foram informados {totn} valores ao todo.')
        print(f'O maior valor informado foi {max(num)}')
    else:
        print(f'Foram informados {totn} valores ao todo.')
        print(f'O maior valor informado foi {totn}.')


# Lista de valores
valores = [0, 3, 1, 5, 9]
valores2 = [4, 7, 0]
valores3 = [1, 2]
valores4 = [6]
valores5 = []

# Chamada da função com a lista desembrulhada
maior(*valores)
maior(*valores2)
maior(*valores3)
maior(*valores4)
maior(*valores5)
