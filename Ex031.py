vel=float(input('Digite a distância da viagem em KM: '))
if vel<=200:
    print('O valor da passagem é de \033[4:31mR${:.2f}.\033[m\nR$0.50 por KM.'.format(vel*0.50))
else:
    print('O valor da passagem é de \033[4:32mR${:.2f}.\033[m\nR$0.45 por KM.'.format(vel*0.45))
