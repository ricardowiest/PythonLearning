from uteis.utilidade import menu
from time import sleep

while True:
    resp = menu.escolha(['VER PESSOAS CADASTRADAS', 'CADASTRAR PESSAOS', 'SAIR'])
    if resp == 1:
        menu.menu('OPÇÃO 1')
        sleep(1)
    elif resp == 2:
        menu.menu('OPÇÃO 2')
        sleep(1)
    elif resp == 3:
        menu.menu(  'SAINDO DO PROGRAMA...')
        sleep(1.5)
        break
    else:
        print('\033[1:31:40mERRO...Digite uma opção válida do menu...\033[m')
        sleep(1)
