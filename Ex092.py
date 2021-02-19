from datetime import date
d=dict()
d['nome']=str(input('Digite o nome: '))
ano=int(input('Digite o ano de nascimento: '))
d['idade']=(date.today().year-ano)
d['ctps']=int(input('Digite carteira de trabalho: [0 não tem] '))
if d['ctps']>0:
    d['contratação']=int(input('Digite o ano de contratação: '))
    d['salário']=int(input('Digite o salário: '))
    d['aposentadoria']=(d['contratação']+35)-ano
print('=-'*30)
for c,k in d.items():
    print(f' - {c} tem o valor {k}')
