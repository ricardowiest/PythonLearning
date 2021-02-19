vel=float(input('Digite a velocidade do carro em Km/h: '))
if vel>80:
    print ('\033[1:30:41mVocê foi multado. Sua multa será no valor de R${:.2f}.\033[m'.format((vel-80)*7.00))
print('Tenho um bom dia!')