frase=str(input('Digite uma frase: ')).upper().strip()
print ('A frase possui \033[4:34m{}\033[m letra(s) A.\n A primeira está na posição \033[1:35m{}\033[m e a ultima na posição \033[1:33m{}\033[m.'.format(frase.count('A'), frase.find('A')+1,frase.rfind('A')+1))
