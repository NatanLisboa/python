#  Desafio 016 - Crie um programa que leia um número real qualquer pelo teclado e mostre na tela a sua porção inteira.

#  from math import trunc

print('Desafio 016 - Quebrando um número')
numeroReal = float(input('Digite um número real (com casas decimais): '))
print('\n', end='')
#  print('O número {} tem a parte inteira {}'.format(numeroReal, trunc(numeroReal)))
print('O número {} tem a parte inteira {}'.format(numeroReal, int(numeroReal)))
