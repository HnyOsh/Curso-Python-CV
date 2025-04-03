def notas(*args, sit=False):
    """
    Def notas(*args, sit=False)
    descubra o total de notas cadastradas, maior nota, menor nota, média e situação
    :param args: Receber vários argumentos(notas)
    :param sit: situação
    :return: retornar dicionario
    """
    n = {}
    n['total'] = len(args)
    n['maior'] = max(args)
    n['menor'] = min(args)
    n['média'] = sum(args) / len(args)
    if sit:
        if n['média'] >= 7:
            n['situação'] = 'BOA'
        elif n['média'] >= 5:
            n['situação'] = 'RAZOÁVEL'
        else:
            n['situação'] = 'RUIM'
    return n


resp = notas(9, 5, 6, 7, 8, 10, 4, sit=True)
print(resp)
help(notas)
