# Mundo 2 - Aula 12 - Condições Aninhadas

# Desafio 042 - Refaça o DESAFIO 035 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será
# formado:

# Equilátero: todos os lados iguais
# Isósceles: dois lados iguais
# Escaleno: Todos os lados diferentes

print('\nDesafio 042 - Analisando Triângulos v2.0\n')
a = float(input('Comprimento da primeira reta (somente números): '))
b = float(input('Comprimento da segunda reta (somente números): '))
c = float(input('Comprimento da terceira reta (somente números): '))

if a < (b + c) and b < (a + c) and c < (a + b):
    print('\nEssas retas podem formar um triângulo ', end='')
    if a == b == c:
        print('EQUILÁTERO')
    elif (a == b or a == c or b == c) and (a != b or a != c or b != c):
        print('ISÓSCELES')
    else:
        print('ESCALENO')
else:
    print('\nEssas retas não podem formar um triângulo')
