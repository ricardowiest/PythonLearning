m1=float(input('Digite a 1ª medida: '))
m2=float(input('Digite a 2ª medida: '))
m3=float(input('Digite a 3ª medida: '))
if m1+m2>m3 and m2+m3>m1 and m1+m3>m2:
    print ('Pode ser formado um triângulo.')
    if m1==m2==m3:
        print ('\033[1:31mEsse triângulo é equilátero.\033[m')
    elif m1!=m2!=m3!=m1:
        print('\033[1:33mEsse triângulo é Escaleno.\033[m')
    else:
        print('\033[1:32mEsse triângulo é Isóceles.\033[m')
else:
    print('Não pode ser formado um triângulo.')
