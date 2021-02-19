lista=list()
while True:
    n=int(input(f'Digite um número: '))
    if n not in lista:
        lista.append(n)
        print ('Valor adicionado.')
    else:
        print('Valor ja inserido...')
    p = str(input('Deseja continuar? [S/N] ')).strip().upper().split()[0]
    while p not in 'SN':
        p = str(input('Inválido. Deseja continuar? [S/N] ')).strip().upper().split()[0]
    if p=='N':
        break
lista.sort()
print(lista)

