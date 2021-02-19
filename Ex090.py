dict=dict()
dict['nome']=str(input('Digite um nome: '))
dict['média']=float(input('Digite a média: '))
print('=-'*30)
if dict['média']>=7:
    dict['situação']='APROVADO'
elif 7>dict['média']>=5:
    dict['situação']='RECUPERAÇÃO'
else:
    dict['situação']='REPROVADO'
for a,b in dict.items():
    print(f'- {a} é igual a {b}')
