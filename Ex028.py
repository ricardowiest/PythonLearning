import random
print ('Adivinhe que número estou pensando...')
num=int(input('\033[1:33mDigite um número entre 0 e 5: '))
comp= random.randint(0, 5)
if comp == num:
    print('Você ganhou!')
else:
    print ('Você perdeu! \nEu pensei no {}'.format(comp))
