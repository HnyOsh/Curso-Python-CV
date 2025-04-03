print('Digite os valor a seguir para calcular o seu IMC')
print('-=-' * 20)
peso = float(input('Digite o seu peso(Kg): '))
altura = float(input('Digite a sua altura(m): '))
imc = peso / (altura ** 2)
if imc < 18.5:
    print('Seu IMC é {:.2f}, você esta abaixo do peso.'.format(imc))
elif imc <= 25:
    print('Seu IMC é {:.2f}, você esta com o peso ideal.'.format(imc))
elif imc <= 30:
    print('Seu IMC é {:.2f}, você esta com sobrepeso.'.format(imc))
elif imc <= 40:
    print('Seu IMC é {:.2f}, você esta com obesidade.'.format(imc))
else:
    print('Seu IMC é {:.2f}, voce esta com obesidade mórbida.'.format(imc))
