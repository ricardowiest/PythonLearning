n=s=c=0
n=int(input('Digite um número qualquer. Digite 999 para sair: \n')) #colocando aqui, não precisaria subtrair no print final.
while n!=999:
    s+=n
    c+=1
    n = int(input('Digite um número qualquer. Digite 999 para sair: \n'))
print ('Você digitou {} números, somando o total de {}.'.format(c,s))
