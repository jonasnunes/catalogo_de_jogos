from random import choice

def jogar():
    
    mensagem_abertura()
    palavra_secreta = carrega_palavra_secreta()
    
    # armazena a quantidade de '_' de acordo com o tamanho da palavra secreta
    letras_acertadas = list('_' * (len(palavra_secreta)))

    print('\nTente descobrir a palavra secreta!\n')
    print(' '.join(letras_acertadas))
    print()

    # armazena todas as letras que já foram escolhidas pelo usuário, excluindo os duplicados
    letras_escolhidas = set()
    # máximo de tentativas para o usuário como o próprio nome da variável já diz. Mas quando acerta a letra o número continua o mesmo na próxima rodada
    maximo_de_tentativas = 5

    while True:

        print(f'\nVocê tem {maximo_de_tentativas} tentativas!')

        # pede um chute ao usuário e depois trata a string colocando em maiúsculo com a função upper() e depois removendo os espaços com a função strip()
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
                # a lista recebe a letra na posição em que foi encontrada, podendo ser mais de uma vez caso haja repetição da letra na palavra
                letras_acertadas[index] = letra.upper()

            index += 1
        
        print('\n', ' '.join(letras_acertadas))

        print()
        print('=' * 60)

        # quando acabar todos os caracteres '_' da lista letras_acertadas é porque o jogador acertou todas as letras e descobriu a palavra
        if '_' not in letras_acertadas:
            print('\nParabéns... Você ganhou o jogo!')
            break
        
        # quando zerar todas as tentativas possíveis o jogo acaba e mostra uma mensagem dizendo qual era a palavra secreta
        if maximo_de_tentativas == 0:
            print('\nEsgotaram-se suas tentativas... Você perdeu!')
            print('\nA palavra secreta era {}'.format(' '.join(palavra_secreta)))
            break
    
    print('\nFim do Jogo!\n')

# FUNÇÕES

def mensagem_abertura():

    print()
    print('*' * 50)
    print('{:*^50}'.format(' Bem Vindo ao Jogo da Forca '))
    print('*' * 50)

def carrega_palavra_secreta():
    
    palavras = []

    # importa o arquivo com as palavras usadas no jogo
    with open('./arquivos/palavras_forca.txt') as arquivo:
        for palavra in arquivo:
            palavra = palavra.strip().upper()
            # adiciona na lista palavras, toda palavra que está no arquivo que está sendo iterado pelo laço for
            palavras.append(palavra)

    '''
        *** Usado para colocar todas as palavras de uma LISTA em maiúsculo ***
        palavra_secreta = [palavra.upper() for palavra in palavras]
    '''
    # escolhe uma palavra aleatoriamente dentro da lista de palavras e atribui à variável palavra_secreta
    palavra_secreta = list(choice(palavras))

    return palavra_secreta


if __name__ == '__main__':
    jogar()