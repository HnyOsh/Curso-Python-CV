frase = str(input("Digite uma frase: ")).strip().upper()

palavras = frase.split()
junto = "".join(palavras)
inverso = ""

#inverso = junto [::-1]

for letra in range(len(junto) - 1, -1, -1):
    inverso += junto[letra]

print(f"O inverso de {frase} é {inverso}")
if inverso == junto:
    print("Temos um palíndromo !")
else:
    print("A frase digitada não é um palíndromo !")

