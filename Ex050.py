s=0
for c in range (0,6):
    n=int(input('Digite um número: '))
    if n%2==0:
        s+=n
print('A soma total dos números pares digitados são {}.'.format(s))
