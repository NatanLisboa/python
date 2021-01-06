#  Desafio 020 - O mesmo professor do desafio anterior quer sortear a ordem de apresentação de trabalhos dos alunos.
#  Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada

from random import shuffle

print('Desafio 020 - Sorteando uma ordem na lista')
aluno1 = input('\nNome do 1º aluno: ')
aluno2 = input('Nome do 2º aluno: ')
aluno3 = input('Nome do 3º aluno: ')
aluno4 = input('Nome do 4º aluno: ')

listaDeAlunos = [aluno1, aluno2, aluno3, aluno4]
shuffle(listaDeAlunos)

print('\nOrdem de apresentação: {}'.format(listaDeAlunos))

print('\n', end='')

