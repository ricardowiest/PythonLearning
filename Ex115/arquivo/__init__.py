def Arquivo(x):
    try:
        a = open(x, 'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True

def criararquivo(x):
    try:
        a = open(x, 'wt+')
        a.close()
    except Exception:
        print('\033[1:31:40mHOUVE UM ERRO NA CRIAÇÃO DO ARQUIVO...\033[m')
    else:
        print(f'\033[1:31mArquivo {x} criado com sucesso!\033[m')
