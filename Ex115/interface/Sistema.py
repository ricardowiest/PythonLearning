from uteis.utilidade import menu
from Ex115.arquivo import *
from time import sleep

arq = 'dados.txt'
if not Arquivo(arq):
    criararquivo(arq)

while True:
    resp = menu.escolha(['VER PESSOAS CADASTRADAS', 'CADASTRAR PESSAOS', 'SAIR'])
    if resp == 1:
        menu.ler(arq)
        sleep(1)
    elif resp == 2:
        menu.menu('Novo Cadastro')
        nome = str(input('Digite o nome: '))
        idade = menu.leiaInt(input('Digite a idade: '))
        menu.cadastro(arq, nome, idade)
        sleep(1)
    elif resp == 3:
        menu.menu('SAINDO DO PROGRAMA...')
        sleep(1.5)
        break
    else:
        print('\033[1:31:40mERRO...Digite uma opção válida do menu...\033[m')
        sleep(1)
