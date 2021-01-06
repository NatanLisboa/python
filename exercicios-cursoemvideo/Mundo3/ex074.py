# Mundo 3 - Aula 16 - Variáveis Compostas - Tuplas

# Exercício Python 074: Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla. Depois disso,
# mostre a listagem de números gerados e também indique o menor e o maior valor que estão na tupla.

from random import randint

maior = menor = 0

print('\nExercício 74 – Maior e menor valores em Tupla\n')

tuplaNumeros = (randint(0, 100), randint(0, 100), randint(0, 100), randint(0, 100), randint(0, 100))

print(f'\nNúmeros gerados: {tuplaNumeros}')
print(f'Maior número da tupla: {max(tuplaNumeros)}')
print(f'Menor número da tupla: {min(tuplaNumeros)}')
