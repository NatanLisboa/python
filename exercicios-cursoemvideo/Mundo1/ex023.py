#  Desafio 023 - Faça um programa que leia um número de 0 a 999 e mostre na tela cada um dos digitos separados

print('\nDesafio 023 - Separando dígitos de um número (como string)')
num = int(input('\nDigite um número: '))
print('\nAnalisando o número {}'.format(num))
print('\nUnidade: {}'.format(num % 10))
print('Dezena: {}'.format(num // 10 % 10))
print('Centena: {}'.format(num // 100 % 10))
print('Unidade de milhar: {}'.format(num // 1000))
