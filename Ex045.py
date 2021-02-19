import random
from time import sleep
print ('Jokenpô Game')
lista=(' ','Pedra','Papel','Tesoura')
comp=random.randint(1,3)
esc=int(input('Faça sua escolha:\n[1] PEDRA\n[2] PAPEL\n[3] TESOURA\nSua escolha: '))
print('Jo...')
sleep(1)
print('Ken...')
sleep(1)
print('Pô!')
print('O computador escolheu {}.'.format(lista[comp]))
print('Você escolheu {}.'.format(lista[esc]))
if comp==1:
    if esc == 1:
        print('EMPATE')
    elif esc == 2:
        print('VOCÊ GANHOU')
    elif esc == 3:
        print('VOCÊ PERDEU')
elif comp==2:
    if esc == 1:
        print('VOCÊ PERDEU')
    elif esc == 2:
        print('EMPATE')
    elif esc == 3:
        print('VOCÊ GANHOU')
elif comp==3:
    if esc==1:
        print('VOCÊ GANHOU')
    elif esc==2:
        print('VOCÊ PERDEU')
    elif esc==3:
        print('EMPATE')
elif esc<1 or esc>3:
    print('OPÇÃO INVÁLIDA!')
