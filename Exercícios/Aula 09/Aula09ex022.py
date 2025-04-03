print('Ola')
nome = str(input('Qual é o seu nome? ')).strip()
print('Seu nome em maiúscula é: {}'.format(nome.upper()))
print('Seu nome com letras minúscula é: {}'.format(nome.lower()))
print('Seu nome contém {} caracteres, sem contar os espaços'.format(len(nome) - nome.count(' ')))
primeiro_nome = nome.split()[0]
print('Seu primeiro nome é {} e ele contém {} caracteres.'.format(primeiro_nome, len(primeiro_nome)))
