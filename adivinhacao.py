from random import randint

def jogar():

    pontos_pessoa = 0
    pontos_computador = 0
    numero_secreto = randint(1, 10)
    rodada = 1


    def verificacaoNumero():
        if numero_pessoa == numero_secreto:
            print('Parabéns... Você acertou e ganhou mais uma tentativa!')
        else:
            print('Que pena :( tente novamente...')


    print('\nBem Vindo ao Jogo da Adivinhação!')
    nivel_dificuldade = int(input('\n[1] Fácil\n[2] Intermediário\n[3] Difícil\n\nEscolha um nível de dificuldade: '))

    while True:
        if nivel_dificuldade == 1:
            tentativas = 10
            break
        elif nivel_dificuldade == 2:
            tentativas = 5
            break
        elif nivel_dificuldade == 3:
            tentativas = 3
            break
        elif nivel_dificuldade < 1 or nivel_dificuldade > 3:
            print('\nNível incorreto! Por favor tente novamente!')
            nivel_dificuldade = int(input('\n[1] Fácil\n[2] Intermediário\n[3] Difícil\nEscolha um nível de dificuldade: '))
            if nivel_dificuldade < 1 or nivel_dificuldade > 3:
                print('\nValor informado incorretamente mais uma vez... Jogo encerrado!')
                exit()

    jogador = input('\nDigite seu nome antes de começar: ')

    print(f'\nRodada: {rodada} de {tentativas}')
    numero_pessoa = int(input('\nDigite um número entre 0 e 10 e tente adivinhar o número que o computador escolheu: '))

    if numero_pessoa < 1 or numero_pessoa > 10:
        print('\nNúmero inválido! Tente novamente...')
        numero_pessoa = int(input('\nDigite um número entre 0 e 10 e tente adivinhar o número que o computador escolheu: '))

        if numero_pessoa < 1 or numero_pessoa > 10:
            print('\nNúmero inválido novamente! Jogo encerrado!')
            exit()

    if numero_pessoa == numero_secreto:
        pontos_pessoa += 1
        tentativas += 1
    else:
        pontos_computador += 1

    print(f'\nVocê digitou {numero_pessoa} e o computador escolheu {numero_secreto}\n')

    verificacaoNumero()

    while rodada < tentativas:
        rodada += 1
        numero_secreto = randint(1, 10)

        print(f'\nRodada: {rodada} de {tentativas}')
        numero_pessoa = int(input('\nDigite um número entre 0 e 10 e tente adivinhar o número que o computador escolheu: '))

        if numero_pessoa == numero_secreto:
            pontos_pessoa += 1
            tentativas += 1
        else:
            pontos_computador += 1

        print(f'\nVocê digitou {numero_pessoa} e o computador escolheu {numero_secreto}\n')

        verificacaoNumero()

        if pontos_pessoa > pontos_computador:
            break

    print(f'\nPlacar Final: {jogador} {pontos_pessoa} ponto(s) x Computador {pontos_computador} ponto(s)\n')

if __name__ == '__main__':
    jogar()