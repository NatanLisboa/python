# Desafio 030 - Crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou ÍMPAR

print('\nDesafio 030 - Par ou Ímpar?')
num = int(input('\nDigite um número inteiro: '))

print('\nO número {} é'.format(num), end=' ')
if num % 2 == 0:
    print('par', end='')
else:
    print('ímpar', end='')
print('!')
