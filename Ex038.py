num1=float(input('Digite um número: '))
num2=float(input('Digite um outro número: '))
print('\033[1:31m= '*30+' Analisando '+'= '*30)
if num1>num2:
    print('\033[1:32mO valor {} é maior que o valor {}.\033[m'.format(num1,num2))
elif num2>num1:
    print('\033[1:33mO valor {} é maior que o valor {}.\033[m'.format(num2,num1))
else:
    print('\033[1:35mNão existe valor maior, ambos são iguais.\033[m')
