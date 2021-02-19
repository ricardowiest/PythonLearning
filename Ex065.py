n=c=s=ma=me=media=0
p ='S'
while p in 'S':
    n = int(input('Digite um número: '))
    s+=n
    c+=1
    if c==1:
        ma=me=n
    else:
        if n>ma:
            ma=n
        elif n<me:
            me=n
    p = str(input('Deseja continuar? [S/N]: ')).strip().upper().split()[0]
media=s/c
print ('Você digitou {} números, somando {}. \nSua média é {}, o maior número foi {} e o menor foi {}.'.format(c,s,media,ma,me))
print('Fim')