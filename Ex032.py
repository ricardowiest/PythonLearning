from datetime import date #importar data
ano=int(input('Digite um ano YYYY: '))
if ano== 0:
    ano=date.today().year #trazer o ano atual
if ano%4==0 and ano%100!=0 or ano%400==0:
    print('\033[1:31:40mAno bissexto\033[m')
else:
    print('\033[1:33:44mAno não bissexto\033[m')
