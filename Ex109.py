from uteis.utilidade import moeda

p = float(input('Digite o preço do produto: '))
print(f'A metade de {moeda.moeda(p)} é {moeda.metade(p, True)}')
print(f'O dobro de {moeda.moeda(p)} é {moeda.dobro(p, True)}')
print(f'Aumentando 10%, temos {moeda.aumento(p, 10, True)}')
print(f'Diminuindo 13%, temo {moeda.dim(p, 13, True)}')
