import random

FORCAIMG = ['''

  +---+
  |   |
      |
      |
      |
      |
=========''', '''

  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''

  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''

  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''

  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''

  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''

  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']

palavras = 'formiga babuino encefalo elefante girafa hamburger chocolate giroscópio'.split()


def main():
    """
    Função Principal do programa
    """
    global FORCAIMG
    print('F O R C A')
    letrasErradas = ''
    letrasAccertadas = ''
    palavraSecreta = geraPalavraAleatória().upper()
    jogando = True
    while jogando:
        imprimeJogo(letrasErradas, letrasAccertadas, palavraSecreta)
        palpite = recebePalpite(letrasErradas + letrasAccertadas)
        if palpite in palavraSecreta:
            letrasAccertadas += palpite
            if VerificaSeGanhou(palavraSecreta, letrasAccertadas):
                print(f'PARABÉNS, a palavra secreta é {palavraSecreta}! Você ganhou!')
                jogando = False
        else:
            letrasErradas += palpite
            if len(letrasErradas) == len(FORCAIMG) -1:
                imprimeJogo(letrasErradas, letrasAccertadas, palavraSecreta)
                print(f'Você excedeu o seu limite de palpites!')
                print(f'Depois de {str(len(letrasErradas))} letras erradas e {str(len(letrasAccertadas))}', end=' ')
                print(f'Palpites corretos, a palavra era {palavraSecreta}')
                jogando = False
        if not jogando:
            if JogarNovamente():
                letrasErradas = ''
                letrasAccertadas = ''
                jogando = True
                palavraSecreta = geraPalavraAleatória()


def geraPalavraAleatória():
    """
    Função que retorna uma string a partir da
    lista de palavras global
    """
    global palavras
    return random.choice(palavras)


def imprimeComEspaços(palavra):
    """
    Recebe uma string palavra ou lista e imprime essa com
    espaço entre suas letras ou strings
    """
    for letras in palavra:
        print(letras, end=' ')
    print()


def imprimeJogo(letrasErradas, letrasAcertadas, palavraSecreta):
    """
    Feito a partir da variável global que contem as imagens
    do jogo em ASCII art, e támbem as letras chutadas de
    maneira correta e as letras erradas e a palavra secreta
    """
    global FORCAIMG
    print(FORCAIMG[len(letrasErradas)]+'\n')
    print('Letras Erradas: ', end='')
    imprimeComEspaços(letrasErradas)
    vazio = '_'*len(palavraSecreta)
    for i in range(len(palavraSecreta)):
        if palavraSecreta[i] in letrasAcertadas:
            vazio = vazio[:i] + palavraSecreta[i] + vazio[i+1:]
    imprimeComEspaços(vazio)


def recebePalpite(palpitesFeitos):
    """
    Função feita para garantir que o usuário coloque uma
    entrada válida, ou seja, que seja uma única letra
    que ele ainda não tenha chutado
    """
    while True:
        palpite = input('Advinhe uma letra. \n')
        palpite.upper()
        if len(palpite) != 1:
            print('Coloque uma única letra.')
        elif palpite in palpitesFeitos:
            print('Você ja chutou essa letra, escolha novamente.')
        elif not 'A' <= palpite <= 'Z':
            print('Por favor escolha apenas letras.')
        else:
            return palpite


def JogarNovamente():
    """
    Função que pede para o usuário decidir se ele quer
    jogar novamente e retorna um booleano representando
    a resposta
    """
    return input('Quer jogar novamente? [sim ou não]\n').upper().startswith('S')
    

def VerificaSeGanhou(palavraSecreta, letrasAcertadas):
    """
    Função que verifica se o usuário acertou todas as
    letras da palavra secreta
    """
    ganhou = True
    for letra in palavraSecreta:
        if letra not in letrasAcertadas:
            ganhou = False
            break
    return ganhou


main()