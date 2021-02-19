from datetime import date
nasc=int(input('\033[:31mDigite seu ano de Nascimento: \033[m'))
data=date.today().year
a=data-nasc
if a<=17:
    saldo=18-a
    print('Abaixo da idade para se alistar.\nFaltam {} anos para o período.\nVocê se alistará em {}.'.format(saldo,(data+saldo)))
elif a==18:
    print('Está no momento de se alistar.')
else:
    saldo=a-18
    print('O período de alistameno ja passou.\nPassaram-se {} anos do período.\nVocê se alistou/deveria se alistar {}'.format(saldo,data-saldo))
