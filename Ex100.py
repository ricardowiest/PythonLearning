from random import randint
from time import sleep

lista = list()
listapar = list()


def soma(cont):
    print('SORTEANDO 5 VALORES DA LISTA: ', end='', flush=True)
    for c in range(0, cont):
        sleep(0.3)
        lista.append(randint(0, 100))
        print(lista[c], end=' ')
    print('\33[1:31:40m Fim \033[m')
    print()


def somapar(x):
    print(f'SOMANDO OS VALORES PARES DE {lista}, TEMOS: ', end=' ')
    for c in lista:
        if c % x == 0:
            listapar.append(c)
    somando= sum(listapar)
    print(somando, '\33[1:31:40m FIM \033[m')


soma(5)
somapar(2)
