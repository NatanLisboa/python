#  Desafio 022 - Crie um programa que leia o nome completo de uma pessoa e mostre:
#  - O nome com todas as letras maiúsculas
#  - O nome com todas as letras minúsculas
#  - Quantas letras ao todo (sem considerar espaços)
#  - Quantas letras têm o primeiro nome

print('Desafio 022 - Analisador de textos')
nome = str(input('\nQual é o seu nome? '))
print('\nNome com todas as letras maiúsculas: {}'.format(nome.strip().upper()))
print('Nome com todas as letras minúsculas: {}'.format(nome.strip().lower()))
print('Quantidade de letras que o nome possui (sem considerar espaços): {}'.format(len(nome.replace(' ', ''))))
nomeDividido = nome.split()
print('Quantidade de letras no primeiro nome ({}): {}'.format(nomeDividido[0], len(nomeDividido[0])))
# print('Quantidade de letras no primeiro nome: {}'.format(nome.strip().find(' ')))
