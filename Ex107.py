from uteis import moeda

p = float(input('Digite o preço do produto: '))
print(f'A metade de R${p:.2f} é R${moeda.metade(p):.2f}')
print(f'O dobro de R${p:.2f} é R${moeda.dobro(p):.2f}')
print(f'Aumentando 10%, temos R${moeda.aumento(p):.2f}')
print(f'Diminuindo 10%, temo R${moeda.dim(p):.2f}')
