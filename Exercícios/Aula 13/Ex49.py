# Variáveis
n1 = int(input("Digite um número: "))

# Texto
print(" ")
print(f"======Tabuada do número {n1}======")
print(" ")

# Looping
for c in range(0, 11):
    tab = c * n1
    print(f'{n1} * {c} = {tab}')
