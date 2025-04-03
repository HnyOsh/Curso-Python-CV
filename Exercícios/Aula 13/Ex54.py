from datetime import datetime
ano_atual = datetime.now().year
SMaior = 0
SMenor = 0

for c in range(0, 7):
    ano = int(input("Em que ano você nasceu ? "))
    if (ano_atual - ano) >= 21:
        SMaior = SMaior + 1
    elif (ano_atual - ano) < 21:
        SMenor = SMenor + 1

print(" ")
print(f"O ano atual é {ano_atual}")
print(f'{SMaior} pessoas já tem mais de 21 anos.')
print(f'{SMenor} pessoas ainda são menores de idade.')
