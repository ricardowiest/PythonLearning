num=int(input('\033[:35mDigite um número: \033[m'))
esc=int(input('Escolha a base do conversão: \n\033[1:31m[1] - BINÁRIO\033[m \n\033[1:32m[2] - OCTAL\033[m \n\033[1:34m[3] - HEXADECIMAL\033[m \nDigite sua escolha: '))
if esc==1:
    print('\033[1:31mO número escolhido, convertido para BINÁRIO é {}.\033[m'.format(bin(esc)))
elif esc==2:
    print('\033[1:32mO número escolhido, convertido para OCTAL é {}.\033[m'.format(oct(esc)))
elif esc==3:
    print('\033[1:34mO número escolhido, convertido para HEXADECIMAL é{}.\033[m.'.format(hex(esc)))
