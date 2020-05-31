def fim(n='<Desconhecido>', g=0):
    print(f'O jogador {n} marcou {g} gol(s) no campeonato.')


nom = str(input('Digite o nome do jogador: '))
go = str(input(f'Quantos gols {nom} fez? '))
if go.isnumeric():
    go = int(go)
else:
    go = 0
if nom.strip() == ' ':
    fim(g=go)
else:
    fim(nom, go)
