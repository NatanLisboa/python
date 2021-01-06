# Mundo 2 - Aula 12 - Condições Aninhadas

# Desafio 036 - Escreva um programa para aprovar um empréstimo bancário para a compra de uma casa. O programa vai
# perguntar o valor da casa, o salário do comprador e em quantos anos ele vai pagar. Calcule o valor da prestação
# mensal, sabendo que ela não pode exceder 30% do salário ou então o empréstimo será negado.

print('\nDesafio 036 - Aprovando Empréstimo\n')
valorCasa = float(input('Qual o valor da casa? R$'))
salarioComprador = float(input('Quanto você ganha por mês? R$'))
anosFinanciamento = int(input('Em quantos anos você pretende pagar esta casa? (somente números): '))

mesesFinanciamento = anosFinanciamento * 12
prestacaoMensal = valorCasa / mesesFinanciamento

print('\n')
if prestacaoMensal > (0.3 * salarioComprador):
    print('\033[31mFinanciamento reprovado\033[m')
    print('''\nCom o seu salário mensal, você não conseguirá quitar esse imóvel dentro de {} anos pagando R${:.2f}/mês
Sentimos muito.'''.format(anosFinanciamento, prestacaoMensal))
else:
    print('\033[32mFinanciamento aprovado\033[m')
    print('\nValor da casa: R${:.2f}'.format(valorCasa))
    print('Salário mensal do comprador: R${:.2f}'.format(salarioComprador))
    print('Tempo de financiamento: {} ano(s)'.format(anosFinanciamento))
    print('\nPrestações mensais: R${:.2f}'.format(prestacaoMensal))
