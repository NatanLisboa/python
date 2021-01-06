# Desafio 045 - Crie um programa que faça o computador jogar Jokenpô com você

from time import sleep
from random import randint


print('\nDesafio 045 - GAME: Pedra Papel e Tesoura\n')
computador = randint(1, 3)
print('1 para \"pedra\"')
print('2 para \"papel\"')
print('3 para \"tesoura\"\n')
jogador = str(input('Escolha sua jogada: '))

if not(jogador.isnumeric()):
    print('\n\033[4;31m{} NÃO ESTÁ ENTRE 1 E 3!\033[m'.format(jogador))
else:
    jogador = int(jogador)

    print('\nJO ', end='')
    sleep(1)
    print('KEN ', end='')
    sleep(1)
    print('PÔ\n')

    if (jogador == 1) and (computador == 1):
        print('\033[33mEMPATOU! VOCÊ E O COMPUTADOR COLOCARAM PEDRA! (PEDRA = PEDRA)\033[m')
    elif (jogador == 1) and (computador == 2):
        print('\033[31mVOCÊ PERDEU! O COMPUTADOR COLOCOU PAPEL! (PEDRA < PAPEL)\033[m')
    elif (jogador == 1) and (computador == 3):
        print('\033[34mPARABÉNS, VOCÊ GANHOU! O COMPUTADOR COLOCOU TESOURA! (PEDRA > TESOURA)\033[m')
    elif (jogador == 2) and (computador == 1):
        print('\033[34mPARABÉNS, VOCÊ GANHOU! O COMPUTADOR COLOCOU PEDRA! (PAPEL > PEDRA)\033[m')
    elif (jogador == 2) and (computador == 2):
        print('\033[33mEMPATOU! VOCÊ E O COMPUTADOR COLOCARAM PAPEL! (PAPEL = PAPEL)\033[m')
    elif (jogador == 2) and (computador == 3):
        print('\033[31mVOCÊ PERDEU! O COMPUTADOR COLOCOU TESOURA! (PAPEL < TESOURA)\033[m')
    elif (jogador == 3) and (computador == 1):
        print('\033[31mVOCÊ PERDEU! O COMPUTADOR COLOCOU PEDRA! (TESOURA < PEDRA)\033[m')
    elif (jogador == 3) and (computador == 2):
        print('\033[34mPARABÉNS, VOCÊ GANHOU! O COMPUTADOR COLOCOU PAPEL! (TESOURA > PAPEL)\033[m')
    elif (jogador == 3) and (computador == 3):
        print('\033[33mEMPATOU! VOCÊ E O COMPUTADOR COLOCARAM TESOURA! (TESOURA = TESOURA)\033[m')
    else:
        print('\033[4;31m{} NÃO ESTÁ ENTRE 1 E 3!\033[m'.format(jogador))
