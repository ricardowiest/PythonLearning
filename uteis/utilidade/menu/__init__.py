from time import sleep


def linha(tam=42):
    return "\033[1:33m-\033[m" * 42


def leiaInt(num):
    while True:
        try:
            n = int(input(num))
        except Exception as erro:
            print(f'\033[1:31:40mERRO: Digite uma opção válida. ERRO TIPO: {erro.__class__}\033[m')
            sleep(1)
            continue
        else:
            return n


def menu(x):
    print(linha())
    print(f"\033[1:30:42m{x.center(42)}\033[m")
    print(linha())


def esc1(x):
    sleep(1.5)
    menu()


def esc2(x):
    sleep(1.5)
    menu()


def escolha(x):  # menu principal
    menu('MENU PRINCIPAL')
    cont = 1
    for c in x:
        print(f'\033[1:32m{cont} - \033[m\033[1:36m{c}\033[m')
        cont += 1
    print(linha())
    opc = leiaInt('\033[1:33mSua OPÇÃO: \033[m')
    return opc
