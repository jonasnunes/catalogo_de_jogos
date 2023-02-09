def jogar():

    print()
    print('*' * 50)
    print('{:*^50}'.format(' Bem Vindo ao Jogo da Forca '))
    print('*' * 50)

    palavra_secreta = 'banana'

    letras_acertadas = list('_' * (len(palavra_secreta)))
    letras_erradas = list()

    enforcou = False
    acertou = False

    print(f'\nTente descobrir a palavra secreta! {letras_acertadas}')

    while not enforcou and not acertou:

        chute = input('\nQual letra? ').lower().strip()

        if chute in letras_acertadas:
            print(f'\nA letra {chute.upper()} já foi escolhida!')

        index = 0

        for letra in palavra_secreta:

            if chute == letra:
                letras_acertadas[index] = letra

            index += 1
        
        print('\n', letras_acertadas)

        if '_' not in letras_acertadas:
            print('\nParabéns... Você acertou a palavra!')
            break


    print('\nFim do jogo!\n')


if __name__ == '__main__':
    jogar()