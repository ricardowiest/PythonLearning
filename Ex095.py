lista = list()
dic = dict()
gols = list()
while True:
    dic.clear()
    gols.clear()
    dic['nome'] = str(input('Digite o nome do Jogador: '))
    j = int(input(f'Quantos jogos {dic["nome"]} jogou? '))
    for c in range(0, j):
        gols.append(int(input(f'Quantos gols na partida {c + 1}? ')))
    dic['gols'] = gols[:]
    dic['total'] = sum(gols)
    lista.append(dic.copy())
    while True:
        r = str(input('Quer continuar? [S/N] ')).upper()[0]
        if r in 'SN':
            break
        if r not in 'SN':
            print('Opção inválida. Digite S ou N ')
    if r == 'N':
        break
print('=*' * 30)
print('Cod. ', end='')
for c in dic.keys():
    print(f'{c:>10}', end=' ')
print()
print('-' * 45)
for c, k in enumerate(lista):
    print(c, end='')
    for d in k.values():
        print(f'      {str(d):<10}', end='')
    print()
print('-' * 45)
while True:
    esc = int(input('Escolha o código do jogador [999 P/ SAIR] '))
    if esc == 999:
        break
    if esc > len(lista):
        print('Código inválido!')
    else:
        print(f'-- Mostrando dados jogador {lista[esc]["nome"]}')
        for c, k in enumerate(lista[esc]["gols"]):
            print(f'No jogo número {c + 1} fez {k} gols.')
        print()
print('Encerrando...')
