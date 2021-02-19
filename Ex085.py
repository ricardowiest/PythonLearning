lista = [[], []]
n=0
for c in range(0,7):
    n=int(input(f'Digite o {c+1} número: '))
    if n % 2 == 0:
        lista[0].append(n)
    else:
        lista[1].append(n)
lista[0].sort()
lista[1].sort()
print(f'Os valores pares digitados são {lista[0]}.\nOs valores ímpares digitados são {lista[1]}.')
