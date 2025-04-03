from random import randint

def jogar():
    computador = randint(0, 10)
    print('Sou seu computador... Acabei de pensar em um número entre 0 e 10.')
    print('Será que você consegue adivinhar qual foi?')

    acertou = False
    palpites = 0

    while not acertou:
        try:
            jogador = int(input('Qual é o seu palpite? '))
            palpites += 1
            if jogador == computador:
                acertou = True
            else:
                if jogador < computador:
                    print('Mais... Tente mais uma vez.')
                else:
                    print('Menos... Tente mais uma vez.')
        except ValueError:
            print("Por favor, insira um número válido entre 0 e 10.")

    print(f'Acertou com {palpites} tentativas. Parabéns!')

def main():
    print('-' * 30)
    print('Bem-vindo ao Jogo da Adivinhação!')
    print('-' * 30)

    jogar()

    while True:
        jogar_novamente = input("Quer jogar novamente? (s/n): ").strip().lower()
        if jogar_novamente == 's':
            jogar()
        elif jogar_novamente == 'n':
            print("Obrigado por jogar! Até a próxima!")
            break
        else:
            print("Opção inválida! Por favor, digite 's' para sim ou 'n' para não.")

if __name__ == "__main__":
    main()
