import adivinhacao, forca

def escolhe_jogo():
    print('O que você quer jogar hoje?')
    print('\n[1] Jogo da Adivinhação [2] Jogo da Forca')
    jogo = int(input('\nQual sua opção? '))

    if jogo == 1:
        adivinhacao.jogar()
    elif jogo == 2:
        forca.jogar()

if __name__ == '__main__':
    escolhe_jogo()