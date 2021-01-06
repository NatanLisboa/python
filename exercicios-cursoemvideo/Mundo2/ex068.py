# Aula 14 - Estrutura de repetição while (Estrutura de repetição com teste lógico)

# Desafio 068 - Faça um programa que jogue par ou ímpar com o computador. O jogo só será interrompido quando o
# jogador perder, mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.

from random import randint
from time import sleep

jogadorEscolha = jogadorQuantidade = '-1'
computadorQuantidade = -1
vitoriasJogador = 0

print('\nDesafio 068 – Jogo do Par ou Ímpar\n')
while True:

    while True:
        jogadorEscolha = str(input('Par ou ímpar? [P/I]: ')).upper().strip()
        if jogadorEscolha == 'P' or jogadorEscolha == 'I':
            break
        else:
            print('\n\033[31mOPÇÃO INVÁLIDA! ESCOLHA "P" PARA PAR OU "I" PARA ÍMPAR.\033[m\n')

    while True:
        jogadorQuantidade = str(input('Quanto você vai colocar? ')).strip()
        if jogadorQuantidade.isnumeric() and (0 <= int(jogadorQuantidade) <= 10):
            break
        else:
            print('\n\033[31mVALOR INVÁLIDO! DIGITE UM VALOR ENTRE 0 E 10.\033[m\n')

    jogadorQuantidade = int(jogadorQuantidade)
    computadorQuantidade = randint(0, 10)

    sleep(1.0)
    print(f'\nVOCÊ COLOCOU {jogadorQuantidade} E O COMPUTADOR COLOCOU {computadorQuantidade}!')
    sleep(2.0)
    print(f'{jogadorQuantidade + computadorQuantidade} É', end=' ')
    if (jogadorQuantidade + computadorQuantidade) % 2 == 0:
        print('PAR', end='')
    else:
        print('ÍMPAR', end='')
    print('!')
    sleep(2.0)
    print('\n', end='')
    if (jogadorQuantidade + computadorQuantidade) % 2 == 0 and jogadorEscolha == 'I':
        print('\033[31mVOCÊ PERDEU DESSA VEZ!\033[m', end=' ')
        break
    elif (jogadorQuantidade + computadorQuantidade) % 2 != 0 and jogadorEscolha == 'P':
        print('\033[31mVOCÊ PERDEU DESSA VEZ!\033[m', end=' ')
        break
    else:
        vitoriasJogador += 1
        print('\033[34mVOCÊ GANHOU! VAMOS JOGAR OUTRA?\033[m')
    print('\n', end='')
    sleep(1.0)

print('\n')
if vitoriasJogador == 0:
    print('QUE AZAR! VOCÊ NÃO GANHOU NENHUMA!')
elif vitoriasJogador == 1:
    print('MAS PELO MENOS VOCÊ GANHOU UMA VEZ!')
else:
    print(f'MAS PELO MENOS VOCÊ GANHOU {vitoriasJogador} VEZES!')
print('OBRIGADO POR JOGAR :)')
