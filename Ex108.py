from uteis.utilidade import moeda

p = float(input('Digite o preço do produto: '))
print(f'A metade de {moeda.moeda(p)} é {moeda.moeda(moeda.metade(p))}')
print(f'O dobro de {moeda.moeda(p)} é {moeda.moeda(moeda.dobro(p))}')
print(f'Aumentando 10%, temos {moeda.moeda(moeda.aumento(p))}')
print(f'Diminuindo 10%, temo {moeda.moeda(moeda.dim(p))}')
