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
    while True:
        try:
            n = int(input(num))
        except Exception as erro:
            print(f'\033[1:31:40mERRO: Digite um valor inteiro válido. ERRO TIPO: {erro.__class__}\033[m')
            continue
        else:
            return n


def leiaReal(x):
    while True:
        try:
            n = float(input(x))
        except Exception as erro:
            print(f'\033[1:31:40mERRO: Digite um valor inteiro válido. TIPO: {erro.__class__}\033[m')
            continue
        else:
            return n
