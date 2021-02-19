pt=int(input('Digite o primeiro termo: '))
r=int(input('Digite a razão: '))
d=pt+(10-1)*r #razão do decimo termo
for c in range (pt,d,r):
    print(c, end=' - ')
