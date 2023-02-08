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
    palavra_inteira = palavra_secreta.copy()
    palavra_string = ''.join(palavra_inteira)

    contador_indices = 0
    
    letras_escolhidas = list()
    barras = list('_' * len(palavra_secreta))
    print(f'\nTente descobrir a palavra secreta: {palavra_string}!\n')

    maximo_de_tentativas = len(palavra_secreta)

    while True:

        print('\n', barras)

        print(f'\nVocê possui {maximo_de_tentativas} tentativas!')

        chute = input('\nQual letra você escolhe? ')

        index = palavra_inteira.index(chute)

        if chute in palavra_secreta:     

            print('\nVocê acertou essa letra! Tente acertar outra!')
            letras_escolhidas.append(chute.upper())
            
            while chute in palavra_secreta:
                palavra_secreta.remove(chute)
                barras.insert(int(chute), index)
                barras.pop()

            if len(palavra_secreta) == 0:
                print('\nVocê descobriu a palavra secreta!')
                print('\n', palavra_string)
                break
                 
        elif chute not in palavra_inteira:    
            print(f'\nA letra {chute.upper()} não pertence a palavra secreta!')
            letras_escolhidas.append(chute.upper())
        
        print('\nLetras já usadas: {}'.format(', '.join(letras_escolhidas)))
            
        #print(f'\nA letra {chute} não faz parte da palavra secreta!')
        maximo_de_tentativas -= 1
        
        if maximo_de_tentativas == 0:
                print('\nVocê não conseguiu adivinhar a palavra secreta!\n')
                break


if __name__ == '__main__':
    jogar()