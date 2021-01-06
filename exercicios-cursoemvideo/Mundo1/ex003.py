#  Desafio 003 - Crie um programa que leia dois números e mostre a soma entre eles

print('\033[7;34;40mDesafio 003 - Soma entre dois números\033[m')
n1 = int(input('1º número: '))
n2 = int(input('2º número: '))
print('{} \033[31m+\033[m {} \033[31m=\033[m \033[4;34m{}\033[m'.format(n1, n2, n1+n2))
