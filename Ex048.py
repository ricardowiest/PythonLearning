s=0
for c in range(1,501):
    if c%3 == 0:
        if c%2!=0:
            s+=c
print('A soma de números ímpares e divisíveis por 3 de 0 até 500 é {}.'.format(s))
