#  Desafio 012 - Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.

print('Desafio 012 - Cálculo do novo preço')
precoOriginal = float(input('Preço original do produto: R$'))
print('\n', end='')
print('Preço do produto com 5% de desconto: R${:.2f}'.format(0.95 * precoOriginal))
