import random
n=0
print('\033[1:32mAdivinhe que número estou pensando...\033[m')
e=random.randint(1,100)
tot=0
acertou= False
while not acertou:
    n=int(input('Escolha um número de 1 até 100: '))
    tot+=1
    if n==e:
        acertou=True
    else:
        if n<e:
            print('\033[1:31mO número que pensei é maior, continue tentando...\033[m')
        else:
            print('\033[1:34mO número que pensei é menor, continue tentando...')
print('O computador pensou {}.\nParabéns, você acertou!\nForam necessário(s) {} tentativa(s).'.format(e,tot))
