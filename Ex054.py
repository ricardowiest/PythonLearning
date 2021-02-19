s1=0
s2=0
from datetime import date
for c in range (1,8):
    d=int(input('Digite a {}º ano de nascimento: '.format(c)))
    a=date.today().year
    m=a-d
    if m>=18 :
        s1+=1
    else:
        s2+=1
print ('{} ano(s) são maiores de idade.\n{} ano(s) são menores de idade.'.format(s1,s2))
