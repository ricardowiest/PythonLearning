lista = list()
for c in range (0,5):
    n=int(input(f'Digite o {c}º número: '))
    '''if c==0:
        lista.insert(0,n)
        print(f'{n} vai para posição 0')
    if c==1:
        if n>lista[0]:
            lista.insert(1,n)
            print(f'{n} vai para posição 1')
        else:
            lista.insert(0,n)
            print(f'{n} vai para posição 0')
    if c==2:
        if n<lista[0]:
            lista.insert(0,n)
            print(f'{n} vai para posição 0')
        if n>lista[0] and n<lista[1]:
            lista.insert(1,n)
            print(f'{n} vai para posição 1')
        else:
            lista.insert(2,n)
            print(f'{n} vai para posição 2')
    if c==3:
        if n<lista[0]:
            lista.insert(0,n)
            print(f'{n} vai para posição 0')
        if n>lista[0] and n<lista[1]:
            lista.insert(1,n)
            print(f'{n} vai para posição 1')
        if n>lista[1] and n<lista[2]:
            lista.insert(2,n)
            print(f'{n} vai para posição 2')
        if n>lista[2]:
            lista.insert(3,n)
            print(f'{n} vai para posição 3')
    if c==4:
        if n<lista[0]:
            lista.insert(0,n)
            print(f'{n} vai para posição 0')
        if n>lista[0] and n<lista[1]:
            lista.insert(1,n)
            print(f'{n} vai para posição 1')
        if n>lista[1] and n<lista[2]:
            lista.insert(2,n)
            print(f'{n} vai para posição 2')
        if n>lista[2] and n<lista[3]:
            lista.insert(3,n)
            print(f'{n} vai para posição 3')
        if n>lista[3]:
            lista.insert(4,n)
            print(f'{n} vai para posição 4')'''
    if c==0 or n>lista[-1]:
        lista.append(n)
        print('Adicionado ao final da lista...')
    else:
        pos=0
        while pos<len(lista):
            if n<=lista[pos]:
                lista.insert(pos,n)
                print(f'Valor adicionado na posição {pos}...')
                break
            pos=+1
print('=-'*30)
print(f'Sua sequência: {lista}')
