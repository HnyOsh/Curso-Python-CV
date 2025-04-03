totp = totn = 0
pmb = ""
menor = None

# Introdução
largura = 40
texto = 'LOJA SUPER BARATÃO'
espacos = (largura - len(texto)) // 2

print('-' * 40)
print(' ' * espacos + texto)
print('-' * 40)

while True:
    np = str(input('Nome do Produto: '))
    preco = float(input('Preço: R$'))
    totn += 1

    # Verifica se o preço é superior a R$1000
    if preco > 1000:
        totp += 1

    # Verifica o menor preço
    if totn == 1 or preco < menor:
        menor = preco
        pmb = np

    # Pergunta se deseja continuar cadastrando produtos
    while True:
        continuar = str(input('Deseja cadastrar outro produto? [S/N] ')).strip().upper()[0]
        if continuar in 'SN':
            break
        print("Entrada inválida. Por favor, digite 'S' para continuar ou 'N' para sair.")

    if continuar == 'N':
        break

# Resultado Final
print(' ')
print('-' * 40)
print(f'Total de produtos cadastrados: {totn}')
print(f'Número de produtos que custam mais de R$1000: {totp}')
print(f'O produto mais barato foi {pmb}, que custa R${menor:.2f}')
