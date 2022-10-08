def jogar(): 
    import random

    print ('********************************')
    print ('Bem vindo! ao jogo de adivinhação')
    print ('********************************')

    #número secreto
    numero_secreto = random.randrange(1 , 101)

    #pontuação
    pontos = 1000

    #tentativas e rodadas
    total_tentativas = 0

    print('Escolha a difilcudade')
    print('(1) Fácil (2) Médio (3) Difícil')

    nivel = int(input('Defina o nível de dificuldade: '))

    if (nivel == 1):
        total_tentativas = 30
    elif (nivel == 2):
        total_tentativas = 20
    else:
        total_tentativas = 10


    rodada = 1
    for rodada in range(1, total_tentativas + 1):
        print('Tentativa {} de {}'.format(rodada,total_tentativas), sep=' ')
        #entrada do user
        chute = input('Digite um numero entre 1 e 100: ')
        chute = int(chute)

        if (chute < 1 or chute > 100):
            print('Você deve digitar um numero entre 1 e 100')
            continue

        #variaveis de verificação
        acertou = chute == numero_secreto
        numero_acima = chute > numero_secreto
        numero_abaixo = chute < numero_secreto

        #verificando chute
        if (acertou):
            print('Você acertou e fez {} pontos'.format(pontos))
            break
        else:
            if (numero_acima):
                print('Você errou! O seu chute foi maior que o número secreto')
            elif (numero_abaixo):
                print('Você errou! O seu chute foi menor que o número secreto')
        pontos_perdidos = abs(numero_secreto - chute )   
        pontos = pontos - pontos_perdidos 

    print('Fim do jogo')

if(__name__ == '__main__'):
    jogar()

