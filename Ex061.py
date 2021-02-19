p=int(input('Primeiro termo: '))
r=int(input('razão: '))
t=p #termo=primeiro
cont=1
while cont<=10:
  print('{} - '.format(t), end=' ')
  t+=r
  cont+=1
