#  Desafio 017 - Faça um programa que leia o comprimento dos dois catetos de um triângulo retângulo, calcule e mostre o
#  comprimento da hipotenusa

from math import sqrt, hypot

print('Desafio 017 - Catetos e Hipotenusa')
b = float(input('Comprimento do 1º cateto (b): '))
c = float(input('Comprimento do 2º cateto (c): '))
#  print('\nHipotenusa (a) = {}'.format(sqrt(pow(b, 2) + pow(c, 2))))
print ('\nHipotenusa (a) = {}'.format(hypot(b, c)))
