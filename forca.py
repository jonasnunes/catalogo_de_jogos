from random import choice

def jogar():
    
    print()
    print('*' * 50)
    print('{:*^50}'.format(' Bem Vindo ao Jogo da Forca '))
    print('*' * 50)

    arquivo = open('./arquivos/palavras_forca.txt', 'r')
    palavras = []

    for palavra in arquivo:
        palavra = palavra.strip().upper()
        palavras.append(palavra)

    arquivo.close()

    '''
        *** Usado para colocar todas as palavras de uma LISTA em maiúsculo ***
        palavra_secreta = [palavra.upper() for palavra in palavras]
    '''
    palavra_secreta = list(choice(palavras))

    # letras_acertadas = ['_' for letra in palavra_secreta]
    letras_acertadas = list('_' * (len(palavra_secreta)))
    letras_escolhidas = set()

    maximo_de_tentativas = 5
    
    print('\nTente descobrir a palavra secreta!\n')
    print(' '.join(letras_acertadas))
    print()

    while True:

        print(f'\nVocê tem {maximo_de_tentativas} tentativas!')

        chute = input('\nQual letra você escolhe? ').upper().strip()

        index = 0

        if chute in palavra_secreta:     

            print('\nVocê acertou essa letra! Tente acertar outra!')
            letras_escolhidas.add(chute)
        
        else:

            print(f'\nA letra {chute} não pertence a palavra secreta!')
            letras_escolhidas.add(chute)
            maximo_de_tentativas -= 1
        
        print('\nLetras escolhidas: {}'.format(', '.join(letras_escolhidas)))
            
        index = 0

        for letra in palavra_secreta:

            if chute == letra:
                letras_acertadas[index] = letra.upper()

            index += 1
        
        print('\n', ' '.join(letras_acertadas))

        print()
        print('=' * 60)

        if '_' not in letras_acertadas:
            print('\nParabéns... Você ganhou o jogo!')
            break

        if maximo_de_tentativas == 0:
            print('\nEsgotaram-se suas tentativas... Você perdeu!')
            print('\nA palavra secreta era {}'.format(' '.join(palavra_secreta)))
            break
    
    print('\nFim do Jogo!\n')


if __name__ == '__main__':
    jogar()