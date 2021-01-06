#  Desafio 010 - Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode
#  comprar. Considere US$1,00 = R$3,27

print('Desafio 010 - Conversor de moedas')
valorEmReal = float(input('Quanto dinheiro você tem na carteira? R$'))
valorEmDolar = valorEmReal / 5.5
valorEmEuro = valorEmReal / 5.93
valorEmLibraEsterlina = valorEmReal / 6.79
print('\n', end='')
print('R${:.2f} = US${:<6.2f}'.format(valorEmReal, valorEmDolar))
print('R${:.2f} = €{:<6.2f}'.format(valorEmReal, valorEmEuro))
print('R${:.2f} = £{:<6.2f}'.format(valorEmReal, valorEmLibraEsterlina))

