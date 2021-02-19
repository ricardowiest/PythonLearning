v=float(input('Digite o valor do imovel R$ '))
t=int(input('Em quantos anos levará para pagar: '))
s=float(input('\033[1:32mDigite seu salário: R$ \033[m'))
p=v/(t*12)
print('\033[2:33:46m= '*35+'Calculando'+'= '*30)
print('\033[1:32:mO valor da prestação será R${:.2f}\033[m'.format(p))
if s*0.30>=p:
    print('\033[1:34mSeu credito foi aprovado!\033[m')
else:
    print('\033[1:31mSeu credito foi NEGADO!')
print('Tenha um bom dia!')