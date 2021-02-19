n=int(input('\033[1:31:44m Digite um número: \033[m'))
print('=*'*30,' T A B U A D A ','=*'*30)
for t in range (0,11):
    print('\033[1:32m{} X {} = {}\033[m'.format(n,t,n*t))
