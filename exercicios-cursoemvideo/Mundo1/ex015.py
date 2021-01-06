#  Desafio 015 - Escreva um programa que pergunte a quantidade de km percorridos por um carro alugado e a quantidade de
#  dias pelos quais ele foi alugado. Calcule o preço a pagar sabendo que o carro custa R$60 por dia e R$0.15 por km
#  rodado

print('Desafio 015 - Aluguel de carros')
print('\n', end='')
diasAluguel = int(input('Por quantos dias o carro foi alugado? '))
kmsRodados = float(input('Quantos quilômetros foram percorridos? '))
precoAluguel = (diasAluguel * 60) + (kmsRodados * 0.15)
print('\n', end='')
print('Preço do aluguel: R${:.2f}'.format(precoAluguel))
