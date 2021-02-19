s=str(input('Digite o sexo [M/F]: ')).strip().upper()[0]
while s not in 'MF':
    print ('Digite [M} para masculino e [F] para feminino.')
    s = str(input('Digite o sexo [M/F] : ')).strip().upper()[0]
print ('Sexo informado: {}'.format(s))
