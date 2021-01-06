#  Desafio 007 - Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre a sua média

print('Desafio 007 - Média entre duas notas')
print('\n', end='')
n1 = float(input('1ª nota do aluno: '))
n2 = float(input('2ª nota do aluno: '))
print('\n', end='')
print('A média entre ', end='')

if n1 >= 6.0:
    print('{}'.format('\033[34m'), end='')
else:
    print('{}'.format('\033[31m'), end='')

print('{}{} e '.format(n1, '\033[m'), end='')

if n2 >= 6.0:
    print('{}'.format('\033[34m'), end='')
else:
    print('{}'.format('\033[31m'), end='')

print('{}{} é igual a '.format(n2, '\033[m'), end='')

if (n1 + n2) / 2 >= 6.0:
    print('{}'.format('\033[34m'), end='')
else:
    print('{}'.format('\033[31m'), end='')

print('{}{}.'.format(((n1+n2) / 2), '\033[m'))
