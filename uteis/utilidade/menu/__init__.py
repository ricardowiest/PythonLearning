from time import sleep


def menu():
    global lista
    lista = list()
    print('-' * 40)
    print(' ' * 10, '\033[1:31:40m MENU PRINCIPAL \033[m')
    print('-' * 40)
    lista = ('Ver as pessoas cadastradas', 'Cadastrar nova pessoa', 'Sair do Sistema')
    for c, k in enumerate(lista):
        print(f'\033[1:33m{c + 1} -\033[m \033[1:32m{k}\033[m')
    print('-' * 40)


def esc1(x):
    print('-' * 40)
    print(' ' * 15, '\033[1:31:40m OPÇÃO 1 \033[m')
    print('-' * 40)
    sleep(1.5)
    menu()


def esc2(x):
    print('-' * 40)
    print(' ' * 15, '\033[1:31:40m OPÇÃO 2 \033[m')
    print('-' * 40)
    sleep(1.5)
    menu()


def esc3(x):
    print('-' * 40)
    print(' ' * 10, '\033[1:31:40m SAINDO DO SISTEMA \033[m')
    print('-' * 40)
    sleep(1.5)


def escolha(x):
    while True:
        esc = 0
        while not 0 < esc < len(lista):
            try:
                esc = int(input(x))
            except Exception as erro:
                print(f'\033[1:30:41mOPÇÃO INVÁLIDA. Digite uma das opções do menu. {erro.__class__}\033[m')
                continue
            else:
                if esc == 1:
                    esc1(x)
                if esc == 2:
                    esc2(x)
                if esc == 3:
                    esc3(x)
                    break
        break
