def leiaInt(num):
    ok = False  # criado para validar
    valor = 0
    while True:
        n = str(input(num))
        if n.isnumeric():
            valor = int(n)
            ok = True
        else:
            print('ERRO! Digite um número válido!')
        if ok:
            break
    return valor


n = leiaInt('Digite um número inteiro: ')
print(f'Você digitou o número {n}.')
