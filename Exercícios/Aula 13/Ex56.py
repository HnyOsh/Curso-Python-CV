somaidade = 0
mediaidade = 0
maioridadehomem = 0
nomevelho = ''
contmul = 0

for c in range(1, 5):
    print(f"-------{c}º PESSOA-------")
    nome = str(input("Qual o seu nome ? ")).strip()
    idade = int(input("Idade: "))
    sexo = str(input("Qual é o seu sexo [M/F] ? ")).strip().upper()
    somaidade += idade
    if c == 1 and sexo in "Mm":
        maioridadehomem = idade
        nomevelho = nome
    if sexo in "Mm" and idade > maioridadehomem:
        maioridadehomem = idade
        nomevelho = nome

mediaidade = somaidade / 4

print(" ")
print("---------------------------------------------")
print(f"A média de idade do grupo é de {mediaidade:.1f} anos")
print(f"O homem mais velho se chama {nomevelho} e tem {maioridadehomem} anos")
print(f"A quantidade de mulheres com menos de 21 anos é {contmul}")
