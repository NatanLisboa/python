# Aula 13 - Estrutura de repetição for

# Desafio 046 - Faça um programa que mostre na tela uma contagem regressiva para o estouro de fogos de artifício, indo
# de dez até 0, com uma pausa de 1 segundo entre eles.

from emoji import emojize
from time import sleep

print('\nDesafio 046 - Contagem regressiva\n')

for i in range(10, -1, -1):
    sleep(1)
    print('{}'.format(i))

print(emojize('\nPEEEEEEW! :fireworks:'))
