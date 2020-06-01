from time import sleep


c = ('\033[n',  # 0 sem cor
     '\033[0:30:41m',  # vermelho
     '\033[0:31:42m',
     '\033[0:32:44m',
     '\033[1:33:41m',
     '\033[7:30m')


def ajuda(com):
    titulo(f'Acessando o manual do comando:  {com} ', 4)
    print(c[5], end='')
    help(com)
    print(c[0], end='')


def titulo(men, cor=0):
    tam = len(men) + 4
    print(c[cor], end='')
    print('~' * tam)
    print(f' {men}')
    print('~' * tam)
    print(c[0], end='')
    sleep(1)


comand = ''
while True:
    titulo('SISTEMA DE INFORMAÇÃO PYTHON HELP', 2)
    comand = str(input('\033[mFunção ou Biblioteca: '))
    if comand.upper() == 'FIM':
        break
    else:
        ajuda(comand)
    titulo('Próximo...', 1)
titulo('Finalizando...até logo!', 3)
