# Desafio 027 - Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome
# separadamente

print('\nDesafio 027 - Primeiro e último nome de uma pessoa')
nome = str(input('\nQual é o seu nome completo? ')).strip()
nome = nome.split()
print('Muito prazer em te conhecer, {} {}!'.format(nome[0], nome[len(nome) - 1]))
