lista= [[0,0,0],[0,0,0],[0,0,0]]
l=c=0
for l in range (0,3):
    for c in range (0,3):
        lista[l][c]=int(input(f'Digite um número para [{l},{c}] : '))
print('=*'*30)
for l in range (0,3):
    for c in range (0,3):
        print(f'[{lista[l][c]}]', end=' ')
    print()
