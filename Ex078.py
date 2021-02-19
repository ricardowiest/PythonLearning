lista=[]
ma=me=0
for c in range(0,5):
    lista.append(int(input(f'Digite o {c}º número da lista: ')))
    if c==0:
        ma=me=lista[c]
    else:
        if lista[c]>ma:
            ma=lista[c]
        if lista[c]<me:
            me=lista[c]
print(f'Sua lista foi {lista}')
print(f'O maior número é {max(lista)} na posição ', end=' ')
for i,v  in enumerate (lista):
    #if v == max(lista):
    if lista[i]==ma:
        print (f'{i}...',end=' ')
print()
print(f'O menor é {min(lista)} na posição ', end=' ')
for i,v in enumerate(lista):
    #if v==min(lista):
    if lista[i]==me:
        print(f'{i}...', end=' ')
print()
