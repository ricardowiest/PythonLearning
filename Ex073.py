print('Lista Brasileirão')
print('-='*50)
br=('Flamengo','Santos','Palmeiras','Grêmio','Atl. Paranaense','São Paulo','Internacional','Corinthians','Fortaleza','Goiás','Bahia','Vasco da Gama','Atl. Mineiro','Fluminense','Botafogo','Ceará','Cruzeiro','Csa','Chapecoense','Avaí')
print(f'Classificação do Brasileirão 2019: {br}')
print('-='*50)
print(f'Os 5 primeiros foram: {br[0:4]}')
print('-='*50)
print(f'Os 4 ultimos são {br[-4:]}')
print('-='*50)
print(f'Os times em ordem alfabetica: {sorted(br)}')
print('-='*50)
print('O time Chapecoense ficou na posição {}ª'.format(br.index('Chapecoense')+1))
print('-='*50)
