n=int(input('Digite um número: '))
t=0
for c in range (1,n+1):
    if n%c==0:
        print('\033[1:31m', end=' ')
        t+=1
    else:
        print('\033[m', end= ' ')
    print('{}'.format(c), end='..')
print ('\n\033[mO número {} foi divisível {} vezes.'.format(n,t))
if t==2:
    print('O número {} É primo.'.format(n))
else:
    print('O número {} NÃO é primo.'.format(n))
