# Aula 13 - Estrutura de repetição for

# Desafio 052 - Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.


print('\nDesafio 052 - Números primos\n')

# Algoritmo 1
'''
divisores = 0
num = int(input('Digite um número inteiro: '))

# Estrutura que verifica a quantidade de divisores do número
print('\n', end='')
for i in range(1, num + 1):
    if num % i == 0:
        divisores += 1
        print('\033[33m', end='')
    else:
        print('\033[31m', end='')
    print('{}\033[m'.format(i), end='  ')

print('\n\n\nO número {} foi dividido por {} números e, por isso, {} '.format(num, divisores, num), end='')
if divisores == 2:
    print('É PRIMO', end='')
else:
    print('NÃO É PRIMO', end='')
print('.')
'''

# Algoritmo 2 (Muito mais eficiente para encontrar números não-primos)
num = int(input('Digite um número inteiro: '))

i = 1

for i in range(2, num + 1):
    if num % i == 0:
        break

print('\n\nO número {} '.format(num), end='')

if i == num and num != 1:
    print('É PRIMO', end='')
else:
    print('NÃO É PRIMO', end='')
print('.')
