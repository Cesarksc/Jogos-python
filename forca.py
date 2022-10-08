def jogar():
    print ('********************************')
    print ('Bem vindo! ao jogo de adivinhação')
    print ('********************************')

    palavra_secreta = 'Banana'
    enforcou = False
    acertou = False

    #enquanto não perdeu e/ou ganhou o jogador irá continuar tentando
    while(not enforcou and not acertou):
        chute = input('Qual letra? ')
        chute = chute.strip()

        index = 1
        for letra in palavra_secreta:
            if (chute.lower() == letra.lower()):
             print('Encontrada a letra {} na posição {}'.format(chute, index))
            index = index + 1

    print('Fim do jogo')

if(__name__ == '__main__'):
    jogar()
