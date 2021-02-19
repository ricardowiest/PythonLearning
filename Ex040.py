n1=float(input('Digite a nota 1: '))
n2=float(input('Digite a nota 2: '))
m=(n1+n2)/2
print('Sua média é {:.2f}'.format(m))
if m<5:
    print ('\033[1:31mVocê foi REPROVADO!\033[m')
elif 7 > m >=5:
    print ('\033[1:33mVocê está em RECUPERAÇÃO!\033[m')
else:
    print ('\033[1:34mVocê está APROVADO!\033[m')