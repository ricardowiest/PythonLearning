def fatorial(num, show=False):
    """"-> Calcula o Fatorial de um número.
    :param n: O número a ser calculado.
    :param show: (opcional) Mostrar ou não a conta.
    :return: O valor de fatorial de um número n."""
    cont = 1
    for c in range(num, 0, -1):
        cont *= c
        if show:
            print(f'{c}', end=' ')
            if c>1:
                print(' x ', end=' ')
            else:
                print(' = ', end=' ')
    return cont


n=int(input('Digite um número para cálculo fatorial: '))
print(fatorial(n, show=True))
