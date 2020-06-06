def metade(x=0, format=False):
    x /= 2
    return x if format is False else moeda(x)


def dobro(x=0, format=False):
    x *= 2
    return x if not format else moeda(x)


def aumento(x=0, tax=0, format=False):
    x = (x * tax / 100) + x
    return x if not format else moeda(x)


def dim(x=0, red=0, format=False):
    x = x - (x * red / 100)
    return x if not format else moeda(x)


def moeda(x=0, moeda='R$'):
    return f'{moeda}{x:>3.2f}'.replace('.', ',')


def resumo(x=0, tax=0 , red=0):
    print('-'*30)
    print('       RESUMO DO VALOR')
    print('-'*30)
    print(f'Preço analisado: \t{moeda(x)}')
    print(f'Dobro do preço: \t{dobro(x , True)}')
    print(f'A metade do preço: \t{metade(x , True)}')
    print(f'{tax}% de aumento: \t{aumento(x, tax , True)}')
    print(f'{red}% de redução: \t\t{dim(x, red, True)}')
    print('-'*30)
