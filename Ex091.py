from random import randint
from time import sleep
from operator import itemgetter #para colocar em ordem um item especifico do dicionário
r=dict()
d={'Jogador 1':randint(1,6),
   'Jogador 2':randint(1,6),
   'Jogador 3':randint(1,6),
   'Jogador 4':randint(1,6)}
print('VALORES SORTEADOS')
for c,k in d.items():
    print(f'O {c} tirou {k} no dado.')
    sleep(1)
print('=-'*16)
print(f'== RANKING DOS JOGADORES ==')
r=sorted(d.items(),key=itemgetter(1),reverse=True) #item para pegar somente o segundo item do dicionario / escol 0 ou 1
for c,k in enumerate(r) :
    print(f'{c+1}º lugar : {k[0]} com {k[1]}')
    sleep(1)
