#  Desafio 014 - Escreva um programa que converta uma temperatura digitada em ºC e converta para ºF

print('Desafio 014 - Conversor de temperatura (Celsius para Fahrenheit)')
c = float(input('Temperatura em ºC (somente números): '))
print('\n{}ºC = {}ºF'.format(c, ((c * 9/5) + 32)))
