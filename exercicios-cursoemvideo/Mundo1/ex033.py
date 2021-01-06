# Desafio 033 - Faça um programa que leia três números e mostre qual é o maior e qual é o menor.

print('\nDesafio 033 - Maior e menor valor')
n1 = int(input('Digite o 1º número: '))
n2 = int(input('Digite o 2º número: '))
n3 = int(input('Digite o 3º número: '))

print('\n')

if n1 > n2:
    if n1 > n3:
        print('Maior número digitado: {}'.format(n1))
        if n2 > n3:
            print('Menor número digitado: {}'.format(n3))
        else:
            print('Menor número digitado: {}'.format(n2))
    else:
        print('Maior número digitado: {}'.format(n3))
        print('Menor número digitado: {}'.format(n2))
else:
    if n2 > n3:
        print('Maior número digitado: {}'.format(n2))
        if n3 > n1:
            print('Menor número digitado: {}'.format(n1))
        else:
            print('Menor número digitado: {}'.format(n3))
    else:
        print('Maior número digitado: {}'.format(n3))
        print('Menor número digitado: {}'.format(n1))
