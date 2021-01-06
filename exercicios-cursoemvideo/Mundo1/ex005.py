# Desafio 005 - Faça um programa que leia um número inteiro e mostre na tela o seu sucessor e seu antecessor

coresLetra = {
             'padrao': '\033[m',
             'vermelho': '\033[31m',
             'verde': '\033[32m',
             'azul': '\033[34m'
        }

print('Desafio 005 - Antecessor e sucessor')
n = int(input('Digite um número inteiro: '))
print('\n')
print('O antecessor de ', end=''
      '{}{}{} é {}{}{}.\n'.format(coresLetra['azul'],
                                  n,
                                  coresLetra['padrao'],
                                  coresLetra['vermelho'],
                                  n - 1,
                                  coresLetra['padrao']))

print('O sucessor de ', end='' 
      '{}{}{} é {}{}{}.'.format(coresLetra['azul'],
                                n, coresLetra['padrao'],
                                coresLetra['verde'],
                                n + 1,
                                coresLetra['padrao']))
