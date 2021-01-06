#  Desafio 018 - Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente des-
#  se ângulo.

from math import sin, cos, tan, radians

print('Desafio 018 - Seno, Cosseno e Tangente')
angulo = (float(input('\nDigite um ângulo de qualquer medida: ')))
print('\n', end='')
print('Seno de {}º = {:.2f}'.format(angulo, sin(radians(angulo))))
print('Cosseno de {}º = {:.2f}'.format(angulo, cos(radians(angulo))))
print('Tangente de {}º = {:.2f}'.format(angulo, tan(radians(angulo))))
