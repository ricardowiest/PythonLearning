from time import sleep
lista=list()
dado=list()
me=n=0
cont='S'
while 'S' in cont:
    dado.append(n)
    dado.append(str(input('NOME: ')))
    dado.append(float(input('Nota 1: ')))
    dado.append(float(input('Nota 2: ')))
    lista.append(dado[:])
    dado.clear()
    n+=1
    cont=' '
    while 'S' not in cont:
        cont=str(input('Deseja continuar? [S/N] ')).upper().strip()[0]
        if cont=='N':
            break
        elif cont!='S':
            print('Opção inválida! ', end=' ')
    print('-'*25)
print()
print('><'*22)
print(f'{"Nº"}{"NOME":>5}{"MEDIA":>15}{"SITUAÇÃO":>17}')
print('-'*41)
for c in range(0,len(lista)):
    media=(lista[c][2]+lista[c][3])/2
    if media>=6:
        sit='APROVADO'
    elif 6>media>=5:
        sit='RECUPERAÇÃO'
    else:
        sit='REPROVADO'
    print(f'{lista[c][0]}{lista[c][1]:>5}{media:>15.2f}{sit:>19}')
print('-'*41)
while True:
    n=int(input('Digite o número do aluno para verificar suas notas: [999 PARA SAIR]\n'))
    if n==999:
        break
    elif n not in range (0,len(lista)):
        print('Número inexistente!', end=' ')
    else:
        print (f'Notas de {lista[n][1]}: \033[1:35n[{lista[n][2]} / {lista[n][3]}]\033[n')
sleep(1)
print('FINALIZANDO!\nVOLTE SEMRPE!')
