def area(a, b):
    tot = a * b
    print(f'A área de um terreno {a} X {b}  é de \33[1:31:40m{tot}m²\33[m')


print('   CONTROLE DE TERRENOS')
print('-' * 30)
l = float(input('Digite a largura (m): '))
c = float(input('Digite o comprimeto (m): '))
area(l, c)
