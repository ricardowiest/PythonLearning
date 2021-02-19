print('-'*50)
print('Loja da Bia')
print('-'*50)
val=nom=soma=v1000=c=vmen=0
nmenor= ' '
while True:
    nom=str(input('Digite o nome do item: ')).upper()
    val=float(input('Digite o valor R$'))
    soma+=val
    c+=1
    if val >=1000:
        v1000+=1
    if c==1 or val<vmen:
        vmen = val
        nmenor = nom
    r=' '
    while r not in 'SN':
        r = str(input('Deseja continuar? [S/N] ')).upper().strip().split()[0]
    if r=='N':
        break
print('-'*50)
print(f'O total da compra foi R${soma:.2f}\nTotal de {v1000} produtos acima de R$1.000,00\nO produto {nmenor} é o mais barato, no valor de R${vmen}')
