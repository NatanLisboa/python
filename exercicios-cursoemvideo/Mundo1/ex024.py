# Desafio 024 - Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com o nome "SANTO".

print('\nDesafio 024 - Verificando as primeiras letras de um texto')
cidade = str(input('\nNome da cidade: '))
# nomeDivididoCidade = cidade.split()
# print('\nA cidade digitada começa com "SANTO": {}'.format(nomeDivididoCidade[0].upper().count('SANTO', 0, 5)))
cidade = cidade.strip()
cidade = cidade.upper()
print('O nome da cidade digitada começa com "SANTO": {}'.format(cidade[:5] == 'SANTO'))
