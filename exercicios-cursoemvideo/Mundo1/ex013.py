#  Desafio 013 - Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento

print('Desafio 013 - Novo salário')
salarioAtual = float(input('Salário atual do funcionário: R$'))
print('\nNovo salário do funcionário (com 15% de aumento): R${:.2f}'.format(1.15 * salarioAtual))
