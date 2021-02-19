from random import randint
print('JOGO PAR OU ÍMPAR')
print('-'*40)
n=c=e=pc=res=0
while True:
    print('=-'*25)
    e=str(input('Deseja par [P] ou ímpar [I}? ')).upper().strip().split()[0]
    n=int(input('Digite um número de sua escolha: '))
    print('-'*50)
    pc=randint(1,10)
    print(f'O computador jogou {pc}')
    res= (n+pc)%2
    soma=n+pc
    if res==0 and e=='P':
        print(f'Você venceu. A soma de {n} + {pc} é {soma}, o resultado é PAR.')
    elif res!=0 and e=='I':
        print(f'Você venceu. A soma de {n} + {pc} é {soma}, o resultado é ÍMPAR.')
    c+=1
    print('Continue a jogar...')
    print('-'*25)
    else:
        break
print (f'Você ganhou {c}X. FIM DE JOGO.')