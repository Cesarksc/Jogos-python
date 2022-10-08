
def jogar():
    import random

    print ('********************************')
    print ('Bem vindo! ao jogo de adivinhação')
    print ('********************************')

    arquivo = open('Frutas.txt', 'r')
    palavras = []

    for linha in arquivo:
        linha = linha.strip()
        palavras.append(linha)
    
    arquivo.close()

    numero = random.randrange(0, len(palavras))
    palavra_secreta = palavras[numero].lower()

    letras_acertadas = ['_' for letra in palavra_secreta]

    enforcou = False
    acertou = False
    erros = 0

    print(letras_acertadas)

    #enquanto não perdeu e/ou ganhou o jogador irá continuar tentando
    while(not enforcou and not acertou):
        chute = input('Qual letra? ')
        chute = chute.strip().lower()

        if(chute in palavra_secreta):
            index = 0
            for letra in palavra_secreta:
                if (chute == letra):
                    letras_acertadas[index] = letra
                index += 1
        else:
            erros += 1

        enforcou = erros == 6
        acertou = '_' not in letras_acertadas
        print(letras_acertadas)

        if acertou:
            print('Você acertou a palavra secreta')
        else:
            print('Você perdeu')


    print('Fim do jogo')

if(__name__ == '__main__'):
    jogar()
