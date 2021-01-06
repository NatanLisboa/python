# Aula 14 - Estrutura de repetição while (Estrutura de repetição com teste lógico)

# Desafio 060 - Faça um programa que leia um número qualquer e mostre o seu fatorial.

from math import factorial

print('\nDesafio 060 - Cálculo do Fatorial\n')
fatorial = 1

numero = 'r'
while not(numero.isnumeric()):
    numero = str(input('Digite um número inteiro positivo para cálculo de seu fatorial: '))
    if not(numero.isnumeric()):
        print('\033[4;31m\nVOCÊ DIGITOU UMA LETRA, UM NÚMERO NEGATIVO OU UM NÚMERO COM VÍRGULA. TENTE NOVAMENTE.\033[m')
        print('\n', end='')

numero = int(numero)
i = numero
print('\n{}! = '.format(numero), end='')
while i > 1:
    print('{}'.format(i), end=' x ')
    fatorial *= i
    i -= 1

print('{} = {} (laço while)'.format(i, fatorial))

fatorial = 1

print('\n{}! = '.format(numero), end='')
for i in range(numero, 1, -1):
    print('{}'.format(i), end=' x ')
    fatorial *= i

print('{} = {} (laço for)'.format(i - 1, fatorial))  # O laço for do Python não atribui o valor à variável se com essa
# atribuição a variável atingir a condição de parada do laço.

fatorial = factorial(numero)

print('\n{}! = {} (função factorial)'.format(numero, fatorial))
