lista=list()
c=0
while True:
    lista.append(int(input('Digite um número: ')))
    r=str(input('Deseja continuar? [S/N] ')).upper().strip().split()[0]
    if r == 'N':
        #c+=1 tirei pois usei o len
        break
    if r not in 'SN':
        r = str(input('Deseja continuar? [S/N] ')).upper().strip().split()[0]
    #c+=1 usei o len
print(f'Você digitou {len(lista)} números.')
lista.sort(reverse=True)
print(f'Sua lista decrescente é {lista}')
if 5 in lista:
    print('O número 5 está na lista.')
else:
    print('O 5 não está na lista.')
