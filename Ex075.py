e=(int(input('Digite um número: ')),
int(input('Digite outro número: ')),
int(input('Digite mais um número: ')),
int(input('Digite um ultimo número: ')))
print(f'Os número escolhidos foram: {e}.\nEm ordem crescente ficará {sorted(e)}')
print (f'O número 9 apareceu {e.count(9)}')
if 3 in e:
    print(f'O número 3 apareceu na posição {e.index(3)+1}')
else:
    print('Não consta número 3 em sua escolha')
print('Os números pares são: ', end=' ')
for c in e:
    if c%2==0:
        print(c, end=' ')
