n1=int(input('\033[1:31mDigite o primeiro número: \033[m'))
n2=int(input('\033[1:32mDigite o segundo número: \033[m'))
n3=int(input('\033[1:34mDigite o terceiro número: \033[m'))
if n1>n2 and n1>n3:
    print('O maior número é ',n1)
if n2>n1 and n2>n3:
    print ('O maior número é ',n2)
if n3>n1 and n3>n2:
    print ('O maior número é ',n3)
if n1<n2 and n1<n3:
    print ('O menor número é ',n1)
if n2<n1 and n2<n3:
    print('O menor número é ',n2)
if n3<n1 and n3<n2:
    print('O menor número é ',n3)
