nome=str(input('Digite seu nome completo: ')).strip()
#maiúsculo
print (nome.upper())
#minúsculo
print(nome.lower())
#contar letras (len) da variável nome retirando espaços
print(len(nome)-nome.count(' '))
#dividir o nome em pedaços criando nova variável
primeiro=nome.split()
#contar a variável do pedaço 0
print(len(primeiro[0]))
