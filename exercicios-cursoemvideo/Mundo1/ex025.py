# Desafio 025 - Crie um programa que leia o nome de uma pessoa e diga se ela tem "SILVA" no nome

print('\nDesafio 025 - Procurando uma string dentro de outra')
nome = str(input('\nQual é o seu nome? ')).strip()
print('\nO nome digitado possui "SILVA": {}'.format('SILVA' in nome.upper()))
