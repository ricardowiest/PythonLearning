num=('zero','um','dois','três','quatro','cinco','seis','sete','oito','nove','dez','onze','doze','treze','quatorze','quinze','dezesseis','dezesete','dezoito','dezenove','vinte')
q='A'
while True:
    while True:
        esc=int(input('Digite um número de 0 até 20: '))
        if 0<=esc<=20:
            break
        print('Tente novamente. ', end=' ')
    print(f'Você digitou o número {num[esc]}')
    while q not in 'SN':
        q=str(input('Deseja Continuar? [S/N] ')).upper().strip()[0].split()
        print ('Escolha incorreta.', end=' ')
        if q=='N':
            break
print('Fim')
