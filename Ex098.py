from time import sleep


def a(x, y, z):
    print('-=' * 20)
    if z < 0:
        z *= -1
    if z == 0:
        z = 1
    print(f'Contagem de {x} até {y} de {z} em {z}')
    sleep(1)
    if x < y:
        c = x
        while c <= y:
            print(c, end=' ', flush=True)
            c += z
            sleep(0.5)
        print('Fim!')
    else:
        c = x
        while c >= y:
            print(c, end=' ', flush=True)
            c -= z
            sleep(0.5)
        print('Fim!')


a(0, 10, 1)
a(10, 0, 2)
print('=-' * 20)
print('Agora é sua vez de personalizar a contagem: ')
b = int(input('Inicio: '))
k = int(input('Fim: '))
d = int(input('Peso: '))
a(b, k, d)
print('\33[1:31:40mFIM DO PROGRAMA...\033[m')
