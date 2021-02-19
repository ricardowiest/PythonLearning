lista=('BREAD',1.50,'RICE',10.40,'BANANA',4.20,'EGGS',5.20, 'ORANGE', 4, 'GRAPE',9.44,'PINEAPLE',5.5,'CHOCOLATE', 12.25)
print('=-'*20)
print(f'{"BEATRIZ STORE":^35}') #centralizado
print('=-'*20)
for pos in range (0,len(lista)): #range do inicio até o ultimo item de lista
    if pos%2==0:
        print(f'{lista[pos]:.<30}', end=' ') #alinhado esquerda
    else:
        print(f'R${lista[pos]:>5.2f}') #alinhando direita
print('=-'*20)