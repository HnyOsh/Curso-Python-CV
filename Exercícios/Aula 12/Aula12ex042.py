print('Analisador de Triângulos')
r1 = float(input('Primeiro segmento: '))
r2 = float(input('Segundo segmento: '))
r3 = float(input('Terceiro segmento: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os segmentos acima PODEM formar um triângulo')
    if r1 == r2 == r3:
        print('O triângulo é Equilátero')
    elif r1 == r2 or r1 == r3 or r2 == r3:
        print('O triângulo é Isósceles')
    else:
        print('O triângulo é Escaleno')
else:
    print('Os segmentos NÃO PODEM formar um triângulo')
