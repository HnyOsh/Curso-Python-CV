pt = int(input("Digite o primeiro termo: "))
r = int(input("Digite a razão: "))
num_termos = 10

for c in range(num_termos):
    pa = pt + c * r
    print(pa, end=" -> ")
