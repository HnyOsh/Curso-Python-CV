print('Verificador de empréstimo bancário.')
print('Digite os valores a seguir para ver se o seu empréstimo bancário sera aprovado ou negado.')
print('-=-' * 30)
valorcasa = float(input('Valor da casa: R$'))
salario = float(input('Salário: R$'))
anos = int(input('Quantos anos desejar pagar: '))
prestacao = valorcasa / (anos * 12)
if prestacao > (0.3 * salario):
    print('\033[31mEMPRESTIMO NEGADO !\033[m O valor da prestação mensal é R${:.2F} '
          'e excedeu os 30% do seu salário.'.format(prestacao))
else:
    print('\033[32mEMPRESTIMO APROVADO !\033[m O valor da prestação mensal é \033[32mR${:.2f}\033[m'.format(prestacao))
