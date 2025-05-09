def aumentar(preco=0, taxa=0, sit=False):
    res = preco + (preco * taxa / 100)
    return res if sit is False else moeda(res)


def diminuir(preco=0, taxa=0, sit=False):
    res = preco - (preco * taxa / 100)
    return res if sit is False else moeda(res)


def dobro(preco=0, sit=False):
    res = preco * 2
    return res if sit is False else moeda(res)


def metade(preco=0, sit=False):
    res = preco / 2
    return res if sit is False else moeda(res)


def moeda(preco=0, simbolo='R$'):  # Alterado o nome do parâmetro para 'simbolo'
    return f'{simbolo}{preco:>.2f}'.replace('.', ',')


def resumo(preco=0, taxaa=10, taxar=5):  # Renomeado o parâmetro 'moeda' para 'simbolo'
    print('-' * 30)
    print('RESUMO DO VALOR'.center(30))
    print('-' * 30)
    print(f'Preço analisado: \t{moeda(preco)}')
    print(f'Dobro do preço: \t{dobro(preco, True)}')
    print(f'Metade do preco: \t{metade(preco, True)}')
    print(f'{taxaa}% de aumento: \t{aumentar(preco, taxaa, True)}')
    print(f'{taxar}% de aumento: \t\t{diminuir(preco, taxar, True)}')
    print('-' * 30)
