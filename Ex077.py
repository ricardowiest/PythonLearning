words='sala','casa','quintal','telhado','piso','cimento','parede'
for c in words: #pega todas as palavras da tupla
    print(f'\nA palavra {c} possui ', end= ' ')
    for letra in c: #pega cada letra de cada palavra da tupla
        if letra in 'aeiou': #analisa se ha vogais na palavra e guarda na variável.
            print (letra, end=' ')
print('Fim...')