s=c=n=0
while True:
    n=int(input('Digite um número. [999 para sair]: '))
    if n==999:
        break
    s+=n
    c+=1
print(f'\033[1:30:41mVocê digitou {c}X. A soma total foi de {s}.\033[m')
