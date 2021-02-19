p=int(input('Primeiro termo: '))
r=int(input('Razão: '))
t=p #termo=primeiro
c=1
tot=0
mais=10
while mais!=0:
  tot+=mais
  while c<=tot:
    print('{} '.format(t),end='')
    print('PAUSA...' if c==mais else '- ', end='')
    t+=r
    c+=1
  mais=int(input('\nQuantos termos a mais você deseja mostrear? '))
print ('Foram mostrados {} termos no total.'.format(tot))
