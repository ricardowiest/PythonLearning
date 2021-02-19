f=str(input('Digite uma frase: ')).strip().lower()
if f==f[::-1]:
    print('Esta frase é um POLÍNDROMO.')
else:
    print('Esta frase não é um POLÍMDROMO.')
