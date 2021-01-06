# Aula 13 - Estrutura de repetição for

# Desafio 055 - Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior e o menor peso
# lidos

maior = 0.0
menor = 0.0

print('\nDesafio 055 - Maior e menor da sequência\n')

for i in range(1, 6):
    peso = float(input('Digite o peso da {}ª pessoa (kg - somente números): '.format(i)))
    if i == 1:
        maior = peso
        menor = peso
    elif peso > maior:
        maior = peso
    elif peso < menor:
        menor = peso

print('\nMaior peso digitado: {:.1f} kg'.format(maior))
print('Menor peso digitado: {:.1f} kg'.format(menor))
