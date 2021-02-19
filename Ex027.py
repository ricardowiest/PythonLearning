n=str(input('Digite seu nome completo: ')).strip()
nome=n.split()
print('Primeiro nome: \033[31m{}\033[m.\nUltimo nome: {}'.format((nome[0]),(nome[-1])))


