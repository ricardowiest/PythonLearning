from time import sleep

def maior(*a):
    cont = ma = 0
    print ('ANALISANDO NÚMEROS...')
    for c in a:
        print(f'{c}', end=' ', flush=True)
        sleep(0.3)
        if cont == 0:
            ma = c
        if c >= ma:
            ma = c
        cont += 1
    print(f'O total de números são {cont} e o maior é \033[1:30:41m {ma} \033[m')


maior(5, 9, 12, 5, 2, 14)
maior(2, 5, 4)
maior(5)
maior(0)
