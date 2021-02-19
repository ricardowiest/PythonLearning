v=float(input('PREÇO DA COMPRA R$'))
op=int(input('FORMA DE PAGAMENTO\n[1] - À vista\n[2] - À vista no cartão\n[3] - Parcelado 2x\n[4] - Parcelado em 3x ou mais\nOPÇÃO: '))
if op==1:
    print('À vista Dinheiro/Cheque 10% - R${:.2f}'.format(v-(v*0.1)))
elif op==2:
    print('À vista no cartão 5% - R${:.2f}'.format(v-(v*0.05)))
elif op==3:
    print('Em até 2X - Preço normal.')
elif op==4:
    print('3X ou mais 20% de juros - R${:.2f}'.format(v+(v*0.2)))
    tot=int(input('Quantas vezes?'))
    print('Para {} parcelas, ficará o valor de R${:.2f} por parcela.'.format(tot,(((v+(v*0.2))/tot))))
else:
    print('OPÇÃO INVALIDA!')
