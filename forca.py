from random import choice

def jogar():
    
    print()
    print('*' * 50)
    print('{:*^50}'.format(' Bem Vindo ao Jogo da Forca '))
    print('*' * 50)

    palavras = (
        'AMARELO', 'AMIGA', 'AMOR', 'AVE', 'BOLO', 'BRANCO', 'CAMA', 'CANECA', 'CELULAR', 'COPO',
        'DOCE', 'ELEFANTE', 'ESCOLA', 'ESTOJO', 'FACA', 'FOTO', 'GARFO', 'GELEIA', 'GIRAFA', 'JANELA',
        'LIMONADA', 'NOITE', 'OCULOS', 'ONIBUS', 'PARQUE', 'PASSARINHO', 'PEIXE', 'PIJAMA', 'RATO',
        'UMBIGO', 'ACENDER', 'AFILHADO', 'AGNOSTICO', 'ARDILOSO', 'ASPERO', 'ASSOMBRACAO', 'ASTERISCO',
        'BALAUSTRE', 'BASQUETE', 'CAMINHO', 'CHAMPANHE', 'CHICLETE', 'CHUVEIRO', 'COELHO', 'CONTEXTO', 
        'CONVIVENCIA', 'CORACAO', 'DESALMADO', 'ELOQUENTE', 'ESFIRRA', 'ESQUERDO', 'FILANTROPO', 
        'GOROROBA', 'HETEROSSEXUAL', 'HORRORIZADO', 'IDIOSSINCRACIA', 'IMPACTO', 'INDEPENDENCIA', 
        'JOCOSO', 'LAUREL', 'MODERNIDADE', 'OFTAMOLOGISTA', 'OTORRINOLARINGOLOGISTA', 'PANACEIA', 
        'PARALELEPIPEDO', 'POROROCA', 'PROGNOSTICO', 'QUARENTENA', 'QUIMERA', 'REFEICAO', 'REPORTAGEM', 
        'SINO', 'TACITURNO', 'TEMPERANCA', 'UFANISMO', 'VISCERA', 'AFOBADO', 'AMENDOIM', 'BANHEIRO', 
        'CAATINGA', 'CACHORRO', 'CAMPEONATO', 'CAPRICORNIO', 'CATAPORA', 'CORRUPCAO', 'CREPUSCULO', 
        'EMPENHADO', 'ESPARADRAPO', 'FORCA', 'GALAXIA', 'HISTORIA', 'MAGENTA', 'MANJERICAO', 'MENTA', 
        'MOEDA', 'PALAVRA', 'PEDREIRO', 'PNEUMONIA', 'PULMAO', 'ROTATORIA', 'SERENATA', 'TRANSEUNTE', 
        'TRILOGIA'
    )

    palavra_secreta = tuple(choice(palavras))

    letras_acertadas = list('_' * (len(palavra_secreta)))
    letras_escolhidas = set()

    maximo_de_tentativas = 5
    
    print('\nTente descobrir a palavra secreta!\n')
    print(' '.join(letras_acertadas))
    print()

    while True:

        print(f'\nVocê tem {maximo_de_tentativas} tentativas!')

        chute = input('\nQual letra você escolhe? ')

        index = 0

        if chute in palavra_secreta:     

            print('\nVocê acertou essa letra! Tente acertar outra!')
            letras_escolhidas.add(chute.upper())
        
        else:

            print(f'\nA letra {chute.upper()} não pertence a palavra secreta!')
            letras_escolhidas.add(chute.upper())
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