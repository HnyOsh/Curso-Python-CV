def fatorial(n, show=False):
    """
    fatorial(n, show=False)
        -> Calcula o Fatorial de um número.
        :param n: O número a ser calculado.
        :param show: (opcional) Mostrar ou não a conta.
        :return: O valor do Fatorial de um número n.
    """
    f = 1
    for c in range(n, 0, -1):
        f *= c
        if show:
            print(f'{c}', end='')
            if c > 1:
                print(' * ', end='')
            else:
                print(' = ', end='')
    return f


# Main part of the code
print('-' * 30)
x = int(input('Deseja saber o fatorial de qual número? '))
s = input('Deseja ver o processo inteiro? [S/N] ').strip().lower()

# Determine if the user wants to see the process
show_process = s == 's'

# Call the function with the correct arguments
print(fatorial(x, show=show_process))
