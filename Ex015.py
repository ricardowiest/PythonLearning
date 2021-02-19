d=int(input('Quantos dias de aluguel? '))
k=float(input('Quantos Quilometros foram rodados? '))
v=(d*60)+(k*0.15)
print('O valor a ser pago é R${:.2f}.'.format(v))
