def leiadin(x): #para valor monetario
    ok = False
    while not ok:
        num = str(input(x)).replace(',', '.').strip()
        if num.isalpha() or num.strip() == '':
            print(f'Erro...{num} não é válido. Digite novamente.')
        else:
            ok = True
            return float(num)


def leiaInt(num):
    ok = False  # criado para validar
    valor = 0
    while True:
        n = str(input(num))
        if n.isnumeric():
            valor = int(n)
            ok = True
        else:
            print('ERRO! Digite um número válido!')
        if ok:
            break
    return valor