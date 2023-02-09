from random import choice

def jogar():
    print('\nBem vindo ao Jogo da Forca\n')

    palavras = [
        'amarelo', 'amiga', 'amor', 'ave', 'bolo', 'branco', 'cama', 'caneca', 'celular', 'copo',
        'doce', 'elefante', 'escola', 'estojo', 'faca', 'foto', 'garfo', 'geleia', 'girafa', 'janela',
        'limonada', 'noite', 'oculos', 'onibus', 'parque', 'passarinho', 'peixe', 'pijama', 'rato',
        'umbigo', 'acender', 'afilhado', 'agnostico', 'ardiloso', 'aspero', 'assombracao', 'asterisco',
        'balaustre', 'basquete', 'caminho', 'champanhe', 'chiclete', 'chuveiro', 'coelho', 'contexto', 
        'convivencia', 'coracao', 'desalmado', 'eloquente', 'esfirra', 'esquerdo', 'filantropo', 
        'gororoba', 'heterossexual', 'horrorizado', 'idiossincrasia', 'impacto', 'independencia', 
        'jocoso', 'laurel', 'modernidade', 'oftamologista', 'otorrinolaringologista', 'panaceia', 
        'paralelepipedo', 'pororoca', 'prognostico', 'quarentena', 'quimera', 'refeicao', 'reportagem', 
        'sino', 'taciturno', 'temperanca', 'ufanismo', 'viscera', 'afobado', 'amendoim', 'banheiro', 
        'caatinga', 'cachorro', 'campeonato', 'capricornio', 'catapora', 'corrupcao', 'crepusculo', 
        'empenhado', 'esparadrapo', 'forca', 'galaxia', 'historia', 'magenta', 'manjericao', 'menta', 
        'moeda', 'palavra', 'pedreiro', 'pneumonia', 'pulmao', 'rotatoria', 'serenata', 'transeunte', 
        'trilogia'
    ]

    palavra_secreta = list(choice(palavras))

    letras_acertadas = list('_' * (len(palavra_secreta)))
    letras_escolhidas = list()
    
    print(f'\nTente descobrir a palavra secreta: {letras_acertadas}!\n')

    while True:

        chute = input('\nQual letra você escolhe? ')

        index = 0

        if chute in palavra_secreta:     

            print('\nVocê acertou essa letra! Tente acertar outra!')
            letras_escolhidas.append(chute.upper())
        
        else:

            print(f'\nA letra {chute.upper()} não pertence a palavra secreta!')
            letras_escolhidas.append(chute.upper())
        
        print(f'\nLetras escolhidas: {letras_escolhidas}')
            
        index = 0

        for letra in palavra_secreta:

            if chute == letra:
                letras_acertadas[index] = letra

            index += 1
        
        print('\n', letras_acertadas)

        print()
        print('=' * 60)

        if '_' not in letras_acertadas:
            print('\nParabéns... Você ganhou o jogo!')
            break
    
    print('\nFim do Jogo!\n')


if __name__ == '__main__':
    jogar()