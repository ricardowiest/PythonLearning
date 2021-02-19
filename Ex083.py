lista=list()
n=str(input('Digite uma expressão: ')).strip()
for c in n:
    if '(' in c:
        lista.append(c)
    elif ')' in c:
        if '(' in lista:
            lista.pop() #para cada ')', é verificado se ja ha na lista algum caractere, então exclui o ultimo pois encontrou seu par.
        else:
            lista.append(c)
            break
if len(lista)==0:
    print (f'Expressão "{n}" é válida!')
else:
    print (f'Expressão "{n}" inválida!')