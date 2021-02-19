from random import randint
from time import sleep
lista=list()
print('-'*50)
print('JOGO MEGA SENA')
print('-'*50)
n=int(input('Quantos jogos de mega sena você deseja? '))
for c in range (0,n):
    for d in range (0,6):
        lista.append(randint(1,60))
    lista.sort()
    print(f'Jogo {c+1}: {lista:^5}')
    lista.clear()
    sleep(1)
print('-='*9,'BOA SORTE', '-='*10)
