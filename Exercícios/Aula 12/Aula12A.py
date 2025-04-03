nome = str(input('Qual o seu nome ? ')).strip().capitalize()
if nome == 'Henry':
    print('\033[1;32mQue nome bonito!\033[m')
elif nome == 'Leticia' or nome == 'Eric' or nome == 'Felipe':
    print('Seu nome é \033[1;33mbem popular\033[m no Brasil.')
else:
    print('Seu nome é bem normal.')
print('Tenha um bom dia, \033[1;34m{}\033[m!'.format(nome))
