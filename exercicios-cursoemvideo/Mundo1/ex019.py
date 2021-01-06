#  Um professor quer sortear um dos seus quatro alunos para apagar o quadro. Faça um programa que ajude ele, lendo o
#  nome deles e escrevendo o nome do escolhido

from random import choice

print('Desafio 019 - Sorteando um item na lista')
aluno1 = input('Nome do 1º aluno: ')
aluno2 = input('Nome do 2º aluno: ')
aluno3 = input('Nome do 3º aluno: ')
aluno4 = input('Nome do 4º aluno: ')
print('\n', end='')
print('Levante-se, {}! Venha apagar o quadro.'.format(choice((aluno1, aluno2, aluno3, aluno4))))
