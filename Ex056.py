mt=0
ii=0
v=0
nv=''
mt=0
for c in range (1,5):
    n=str(input('Digite seu nome:')).strip()
    i=int(input('Digite sua idade: '))
    ii+=i
    s=str(input('Digite seu sexo M ou F: ')).strip().lower()
    if c==1 and s=='m':
        v=i
        nv=n
    if i>v and s=='m':
        nv=n
        v=i
    if s=='f' and i<20:
        mt+=1
print ('A média de idade é do grupo é {:.1f}.'.format(ii/4))
print('O homem mais velho é {} e possui {} anos.'.format(nv,v))
print ('{} mulhere(s) possuem menos de 20 anos. '.format(mt))
