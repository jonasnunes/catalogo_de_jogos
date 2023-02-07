def jogar():
    print('\nBem vindo ao Jogo da Forca')

    palavra_secreta = list('paralelepipedo')
    barras = list('_' * len(palavra_secreta))
    print('\nTente descobrir a palavra secreta!\n')
    print(' '.join(barras), '\n')

    maximo_de_tentativas = len(palavra_secreta)

    while True:

        print(f'\nVocê possui {maximo_de_tentativas} tentativas!')

        letras_corretas = list()
        letras_erradas = list()

        chute = input('\nQual letra você escolhe? ')

        if chute in palavra_secreta:
            maximo_de_tentativas -= 1
            print('\nVocê acertou essa letra! Tente acertar outra!')
            
            while chute in palavra_secreta:
                letras_corretas.append(chute)
                palavra_secreta.remove(chute)

            if len(palavra_secreta) == 0:
                print('Você descobriu a palavra secreta!')
                break
            else:
                continue

        else:
            print(f'\nA letra {chute} não faz parte da palavra secreta!')
        
        if chute not in palavra_secreta:
            maximo_de_tentativas -= 1

            if maximo_de_tentativas == 0:
                print('Você não conseguiu adivinhar a palavra secreta!')
                break
    
    print('Você perdeu!')


if __name__ == '__main__':
    jogar()