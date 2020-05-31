from datetime import date


def voto(x):
    data = (date.today().year - ano)
    print(f'Com {data} anos:', end=' ')
    if data < 16:
        return 'NEGADO'
    elif data > 65:
        return 'OPCIONAL'
    else:
        return 'OBRIGATÓRIO'


ano = int(input('Digite seu ano de nascimento: '))
print(f'{voto(ano)}')
