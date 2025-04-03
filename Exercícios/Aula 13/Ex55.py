maiorpeso = 0
menorpeso = 0

for c in range(1, 6):
    peso = float(input(f"{c}º Peso: "))
    if c == 1:
        maiorpeso = peso
        menorpeso = peso
    else:
        if peso > maiorpeso:
            maiorpeso = peso
        if peso < menorpeso:
            menorpeso = peso

print(f"Maior peso: {maiorpeso} kg")
print(f"Menor peso: {menorpeso} kg")
