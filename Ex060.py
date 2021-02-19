'''from math import factorial
n=int(input('Digite um número: '))
f=factorial(n)
print('O Fatorial de {} é {}.'.format(n,f))'''

'''n=int(input('Digite um número: '))
f=1
c=n
while c>0:
  print('{} '.format(c), end=' ')
  print('X ' if c>1 else '= ', end=' ')
  f*=c
  c-=1
print('{}'.format(f))'''

n=int(input('Digite um número '))
f=1
for c in range (n,0,-1):
  f*=c
print(f)