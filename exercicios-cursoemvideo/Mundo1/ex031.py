# Desafio 031 - Desenvolva um programa que pergunte a distância de uma viagem em km. Calcule o preço da passagem, co -
# brando R$0,50 por km para viagens de até 200 km e R$0,45 para viagens mais longas

print('\nDesafio 031 - Custo da Viagem')
distanciaViagem = float(input('\nDistância da viagem (em km): '))

preco = distanciaViagem * 0.5 if distanciaViagem <= 200 else distanciaViagem * 0.45

print('Para uma viagem de {} km, o preço da passagem será de R${:.2f}'.format(distanciaViagem, preco), end='')
