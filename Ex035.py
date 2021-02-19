m1=float(input('Digite a 1ª medida: '))
m2=float(input('Digite a 2ª medida: '))
m3=float(input('Digite a 3ª medida: '))
if m1+m2>m3 and m2+m3>m1 and m1+m3>m2:
    print ('Pode ser formado um triângulo.')
else:
    print('Não pode ser formado um triângulo.')
