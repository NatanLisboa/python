# Mundo 2 - Aula 12 - Condições Aninhadas

# Desafio 038 - Escreva um prgrama que leia dois números inteiros e compare-os, mostrando na tela uma mensagem:

# - O primeiro valor é maior
# - O segundo valor é maior
# - Não existe valor maior, os dois são iguais

print('\nDesafio 038 - Comparando números\n')
n1 = int(input('1º número: '))
n2 = int(input('2º número: '))

print('\n')
if n1 > n2:
    print('O primeiro valor é maior ({} > {}).'.format(n1, n2))
elif n2 > n1:
    print('O segundo valor é maior ({} < {}).'.format(n1, n2))
else:
    print('Não existe valor maior, os dois são iguais ({} = {}).'.format(n1, n2))
