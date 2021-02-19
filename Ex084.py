lista=list()
dado=list()
r='S'
ma=me=0
while 'S' in r:
    dado.append(str(input('Digite o nome: ')))
    dado.append(int(input('Digite o peso em KG: ')))
    if len(lista)==0:
        ma=me=dado[1]
    else:
        if dado[1]>ma:
            ma=dado[1]
        if dado[1]<me:
            me=dado[1]
    lista.append(dado[:])
    dado.clear()
    r=str(input('Deseja continuar? [S/N] ')).upper().strip()[0]
    if r not in 'SN':
        print('Dado inválido!')
        r=str(input('Deseja Continuar? [S/N]')).upper().strip()[0]
    elif r=='N':
        break
print(f'Você digitou o total de {len(lista)} cadastros.')
print(f'O maior peso é {ma}  de ', end=' ')
for c in lista:
    if c[1]==ma:
        print(f'{c[0]} ', end=' ')
print()
print(f'O menor número é {me} de ', end=' ')
for c in lista:
    if c[1]==me:
        print(f'{c[0]}', end=' ')
print()
