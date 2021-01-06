# Desafio 026 - Faça um programa que leia uma frase pelo teclado e mostre:
# - Quantas vezes aparece a letra "A"
# - Em que posição ela aparece a primeira vez
# - Em que posição ela aparece a última vez

print('\nDesafio 026 - Primeira e última ocorrência de uma string')
frase = str(input('\nDigite uma frase: ')).strip()
print('\nOcorrências da letra "A": {}'.format(frase.upper().count('A')))
print('Posição da primeira ocorrência de "A": {}'.format(frase.upper().find('A') + 1))
print('Posição da última ocorrência de "A": {}'.format(frase.upper().rfind('A') + 1))
