# Solicitando valor para o cliente
print(' ')
preco = float(input('Digite o preço do produto para verificar o valor nas condições de pagamentos : R$'))
print(' ')

# Calculando os valores nas condições de pagamento
vista = preco - preco * 10 / 100
cartao = preco - preco * 5 / 100
cartao2x = preco / 2


# Exibindo as condições de pagamento
print('Qual o método de pagamento ?')
print(' ')
print('1- Pagamento à vista com dinheiro ou cheque - \033[32m10% de desconto\033[m')
print('2- Pagamento à vista no cartão - \033[32m5% de desconto\033[m')
print('3- Pagamento em até 2x no cartão - \033[33mparcelamento sem juros\033[m')
print('4- Pagamento no cartão em 3x ou mais - \033[31m20% de juros\033[m')
print(' ')

# Opção de Pagamento
opcao = int(input('Escolha uma opção: '))
print(' ')

# Exibindo o valor de pagamento
if opcao == 1:
    print('O valor do pagamento à vista é \033[32mR${:.2f}\033[m'.format(vista))
elif opcao == 2:
    print('O valor do pagamento à vista no cartão é \033[32mR${:.2f}\033[m'.format(cartao))
elif opcao == 3:
    print('O valor do pagamento parcelado em 2x são \033[33m2 parcelas de R${:.2f}\033[m'.format(cartao2x))
elif opcao == 4:
    parcela = int(input('Digite o número de parcelas: '))
    print(' ')
    if parcela > 3:
        vp = (preco + preco * 20 / 100) / parcela
        print('O valor do pagamento parcelado em {}x são \033[31m{} parcelas de R${:.2f}\033[m'
              .format(parcela, parcela, vp))
    else:
        print('\033[31mOpção Inválida, o número de parcelas tem que ser 3 ou mais\033[m')
else:
    print('\033[31mOpção Invalida ! \033[m')
