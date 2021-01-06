# Desafio 028 - Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5 e peça para o usuá -
# rio tentar descobrir qual foi o número escolhido pelo computador. O programa deverá escrever na tela se o usuário ven-
# ceu ou perdeu.

from random import randint
from time import sleep

print('\nDesafio 028 - Jogo da Advinhação v.1.0')
numeroComputador = randint(0, 5)
print('\nVou pensar em um número entre 0 e 5...')
sleep(3)
numeroUsuario = str(input('\nEm qual número pensei: ')).strip()

if not(numeroUsuario.isnumeric()):
    print('Você não digitou um valor numérico! Reinicie o programa e tente novamente.')
else:
    numeroUsuario = int(numeroUsuario)
    if not((numeroUsuario >= 0) and (numeroUsuario <= 5)):
        print('Você não digitou um número entre 0 e 5! Reinicie o programa e tente novamente.')
    else:
        sleep(1)
        print('\nPROCESSANDO...')
        sleep(3)
        if numeroUsuario == numeroComputador:
            print('Parabéns, você venceu! Eu pensei no mesmo número que você.')
        else:
            print('Me desculpe, você perdeu! Eu pensei no número {}.'.format(numeroComputador))
