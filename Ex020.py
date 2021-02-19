from random import shuffle
a=str(input('Digite o nome do primeiro aluno: '))
b=str(input('Digite o nome do segundo aluno: '))
c=str(input('Digite o nome do terceiro aluno: '))
d=str(input('Digite o nome do quarto aluno: '))
lista=[a,b,c,d]
#não abriu nova variável, shuffle embaralha a lista.
shuffle(lista)
print('A ordem de apresentação será \n{}'.format(lista))
