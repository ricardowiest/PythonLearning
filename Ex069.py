print('PROGRAMA DE CADASTRO DE PESSOAS')
i=id=sm=mm=0
while True:
    print('-'*30)
    print('CADASTRE UMA PESSOA.')
    print('-'*30)
    i=int(input('Digite a idade: '))
    if i>=18:
        id=+1
    s = ' '
    while s not in 'MF':
        s=str(input('Digite o sexo: [M/F] ')).upper().strip().split()[0]
    if s=='M':
        sm=+1
    elif s=='F' and i<=20:
        mm+=1
    e=' '
    while e not in 'SN':
        e = str(input('DESEJA CONTINUAR? [S/N]  ')).strip().upper().split()[0]
    if e=='N':
        break
print('-'*30)
print(f'TOTAL DE PESSOAS COM MAIS DE 18 ANOS: {id}\nTotal de {sm} homem(ns) cadastrado(s).\nTotal de {mm} mulheres menores cadastradas.')
