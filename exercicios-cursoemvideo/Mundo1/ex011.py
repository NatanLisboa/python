#  Desafio 011 - Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quanti -
#  dade de tinta necessária para pintá-la, sabendo que cada litro de tinta pinta uma área de 2m^2

print('Desafio 011 - Pintura de uma parede')
largura = float(input('Largura da parede (em m): '))
altura = float(input('Altura da parede (em m): '))
print('\n', end='')
print('Área da parede: {} m²'.format(largura * altura))
print('Quantidade de tinta necessária: {} L'.format(largura * altura / 2))
