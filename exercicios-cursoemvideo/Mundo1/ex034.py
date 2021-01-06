# Desafio 034 - Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento
# - Para os salários superiores a R$1250,00, calcule um aumento de 10%.
# - Para os inferiores ou iguais, o aumento é de 15%.

print('\nDesafio 034 - Aumentos múltiplos')
salarioFuncionario = float(input('\nDigite o valor do seu salário: R$'))

print('\n\nSalário antigo: R${:.2f}'.format(salarioFuncionario))
if salarioFuncionario > 1250.0:
    salarioFuncionario += (0.1 * salarioFuncionario)
else:
    salarioFuncionario += (0.15 * salarioFuncionario)

print('Novo salário: R${:.2f}'.format(salarioFuncionario))
