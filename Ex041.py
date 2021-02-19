from datetime import date
ano=int(input('Digite o ano de nascimento do jogador: '))
t=date.today().year
calc=t-ano
if calc<=9:
    print('\033[1:31mMIRIM\033[m')
elif 14 > calc >=9:
    print('\033[1:32mINFANTIL\033[m')
elif 19> calc >=14:
    print('\033[1:36mJUNIOR\033[m')
elif 25>calc>=19:
    print('\033[1:34mSÊNIOR\033[m')
else:
    print('\033[1:35mMASTER\033[m')