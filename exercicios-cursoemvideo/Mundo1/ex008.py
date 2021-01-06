#  Desafio 008 - Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros

print('Desafio 008 - Conversor de medidas')
valorEmMetros = float(input('Digite um valor em metros: '))
print('\n{} m = {} km'.format(valorEmMetros, valorEmMetros / 1000))
print('{} m = {} hm'.format(valorEmMetros, valorEmMetros / 100))
print('{} m = {} dam'.format(valorEmMetros, valorEmMetros / 10))
print('{} m = {} dm'.format(valorEmMetros, valorEmMetros * 10))
print('{} m = {} cm'.format(valorEmMetros, valorEmMetros * 100))
print('{} m = {} mm'.format(valorEmMetros, valorEmMetros * 1000))
