lista= [[0,0,0],[0,0,0],[0,0,0]]
l=c=par=ma=soma=0
for l in range (0,3):
    for c in range (0,3):
        lista[l][c]=int(input(f'Digite um número para [{l},{c}] : '))
        if lista[l][c]%2==0:
            par+=lista[l][c]
print('=*'*30)
for l in range (0,3):
    for c in range (0,3):
        print(f'[{lista[l][c]}]', end=' ')
    print()
print('=*'*30)
print(f'A soma dos números pares é {par}.')
for l in range(0,3):
    soma+=lista[l][2]
print(f'A soma da terceira coluna é {soma}.')
for c in range(0,3):
    if c==lista[1][c]:
        ma=lista[1][c]
    else:
        if lista[1][c]>ma:
            ma=lista[1][c]
print(f'O maior valor da segudna linha é {ma}')
