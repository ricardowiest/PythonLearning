lista=list()
pa=list()
im=list()
while True:
    '''n=int(input('Digite um número: '))
    lista.append(n)
    if n%2==0:
        pa.append(n)
    else:
        im.append(n)
    r=str(input('Deseja continuar? [S/N] ')).upper().strip().split()[0]
    if r == 'N':
        #c+=1 tirei pois usei o len
        break
    if r not in 'SN':
        r = str(input('Deseja continuar? [S/N] ')).upper().strip().split()[0]
    #c+=1 usei o len'''
    lista.append(int(input('Digite um número: ')))
    r = str(input('Deseja continuar? [S/N] ')).upper().strip().split()[0]
    if r == 'N':
        # c+=1 tirei pois usei o len
        break
    if r not in 'SN':
        r = str(input('Deseja continuar? [S/N] ')).upper().strip().split()[0]
for c,v in enumerate(lista):
    if v%2==0:
        pa.append(v)
    else:
        im.append(v)
print(f'A lista completa é: {lista}')
print(f'A lista de pares é {pa}')
print(f'A lista de ímpares é {im}')


