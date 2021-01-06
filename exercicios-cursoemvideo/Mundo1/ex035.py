# Desafio 035 - Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se eles podem ou não
# formar um triângulo

print('\nDesafio 035 - Analisando Triângulo v1.0')

a = float(input('\nComprimento da primeira reta (a): '))
b = float(input('Comprimento da segunda reta (b): '))
c = float(input('Comprimento da terceira reta (c): '))

print('\n')

print('Essas retas', end=' ')
if (a < (b + c)) and (b < (a + c)) and (c < (a + b)):
    if (a != b) and (a != c) and (b != c):
        print('podem formar um triângulo ESCALENO.')
    else:
        if ((a == b) or (a == c) or (b == c)) and ((a != b) or (a != c) or (b != c)):
            print('podem formar um triângulo ISÓSCELES.')
        else:
            print('podem formar um triângulo EQUILÁTERO.')
else:
    print('NÃO podem formar um triângulo :(')
