from time import sleep
n=d=0
while True:
    n=int(input('\033[1:36:40m Digite um número para sua tabuada: \033[m'))
    print('-'*50)
    if n<0:
        break
    for c in range (1,11):
        t=c*n
        print(f'\033[1:32m{n} X {c} = {t}\033[m')
    print('-'*50)
    d+=1
print(f'\033[1:31:40m{d} tabuadas foram mostradas.\033[m')
print('\033[1:33mENCERRANDO PROGRAMA...\033[m')
sleep(1)