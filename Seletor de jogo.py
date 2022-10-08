import Adivinhacao
import forca

print ('*******************************')
print ('***** Escolha o seu jogo! *****')
print ('*******************************')

print('(1) Forca (2) Adivinhação')

jogo = int(input("Selecionar jogo: "))

if (jogo == 1):
    forca.jogar()
else:
    Adivinhacao.jogar()