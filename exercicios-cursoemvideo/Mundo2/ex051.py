# Aula 13 - Estrutura de repetição for

# Desafio 051 - Desenvolva um programa que leia o primeiro termo e a razão de uma PA. No final, mostre os 10 primeiros
# termos dessa progressão

print('\nDesafio 051 - Progressão Aritmética\n')
a1 = int(input('Primeiro termo da PA: '))
r = int(input('Razão da PA: '))

print('\nProgressão aritmética: ', end='')
for an in range(a1, a1 + 10 * r, r):
    print('{} '.format(an), end='')

print('\n')
