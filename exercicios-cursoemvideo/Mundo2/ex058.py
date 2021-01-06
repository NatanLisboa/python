
# Aula 14 - Estrutura de repetição while (Estrutura de repetição com teste lógico)

# Desafio 058 - Melhore o jogo do DESAFIO 028 onde o computador vai pensar em um número entre 0 e 10. Só que agora o
# jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer.

from random import randint
from time import sleep

print('Desafio 058 - Jogo da Adivinhação v2.0')
computador = randint(0, 10)
jogador = -1
tentativas = 0
print('\033[33m\nPENSEI EM UM NÚMERO ENTRE 0 E 10\033[m\n')
while computador != jogador:
    jogador = str(input('Em qual número pensei? (ENTRE 0 E 10): '))
    print('\n')
    sleep(0.5)
    if not(jogador.isnumeric()):
        print('\033[4;31mVOCÊ NÃO DIGITOU UM NÚMERO INTEIRO ENTRE 0 E 10! TENTE NOVAMENTE.\033[m\n')
    elif int(jogador) > 10:
        print('\033[4;31mVOCÊ DIGITOU UM NÚMERO MAIOR QUE 10! TENTE NOVAMENTE.\033[m\n')
    else:
        jogador = int(jogador)
        tentativas += 1
        print('\033[33mPROCESSANDO...\033[m')
        print('\n', end='')
        if jogador > computador:
            print('MENOS! TENTE OUTRA VEZ!\n')
        elif jogador < computador:
            print('MAIS! TENTE OUTRA VEZ!\n')
print('\n\n\033[34m', end='')
if tentativas > 1:
    print('PARABÉNS, EU PENSEI MESMO NO NÚMERO {}. VOCÊ ACERTOU COM {} TENTATIVAS!'.format(computador, tentativas))
else:
    print('IMPRESSIONANTE! VOCÊ ADIVINHOU COM APENAS UMA TENTATIVA! PARABÉNS.')
