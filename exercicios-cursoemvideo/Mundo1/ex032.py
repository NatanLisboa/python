# Desafio 032 - Faça um programa que leia um ano qualquer e mostre se ele é bissexto

from datetime import date

print('\nDesafio 032 - Ano Bissexto')
ano = int(input('\nDigite um ano qualquer (Insira 0 para analisar o ano atual): '))

print('\n')
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('O ano {} é bissexto'.format(ano))
else:
    print('O ano {} NÃO é bissexto'.format(ano))
