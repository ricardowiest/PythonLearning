sal=float(input('Digite o salário R$'))
if sal>1250:
    print('\033[1:34mO novo salário terá reajuste de 10%. Totalizando R${:.2f}\033[m'.format((sal*0.10)+sal))
else:
    print('\033[1:31mO novo salário terá reajuste de 15%. Totalizando R${:.2f}\033[m'.format((sal*0.15)+sal))
