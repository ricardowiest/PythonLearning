from time import sleep
n1=int(input('Digite o 1º número: '))
n2=int(input('Digite o 2º número: '))
esc=0
while esc!=5:
    esc=int(input('''   Digite a opção de sua escolha: 
    [1] somar
    [2] multiplicar
    [3] maior
    [4] novos números
    [5] sair do programa
    Sua escolha: '''))
    if esc==1:
        print('A soma dos dois números é {}.'.format(n1+n2))
    elif esc==2:
        print('A multiplicação dos dois números é {}.'.format(n1*n2))
    elif esc==3:
        if n1>n2:
            print('O maior número é {}'.format(n1))
        else:
            print('O maior número é {}.'.format(n2))
    elif esc==4:
        n1=int(input('Digite o 1º número: '))
        n2=int(input('Digite o 2º número: '))
    elif esc==5:
        print('Finalizando...')
    else:
        print('OPÇÃO INVÁLIDA...')
    sleep(2)
    print('*-*'*30)
print ('FIM DO PROGRAMA!')