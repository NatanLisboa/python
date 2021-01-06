# Desafio 043 - Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu IMC e mostre seu status, de
# acordo com a tabela abaixo:

# - Abaixo de 18.5: Abaixo do peso
# - Entre 18.5 e 25: Peso ideal
# - 25 até 30: Sobrepeso
# - 30 até 40: Obesidade
# - Acima de 40: Obesidade mórbida

print('\nDesafio 043 - Índice de Massa Corporal\n')
nome = str(input('Qual é o seu nome? '))
peso = float(input('Quanto você pesa, {}? (kg): '.format(nome)))
altura = float(input('Qual é a sua altura, {}? (m): '.format(nome)))

imc = peso / altura ** 2

print('\nSeu IMC: {:.1f}'.format(imc))
if imc < 18.5:
    print('Tome cuidado, {}! Você está abaixo do peso.'.format(nome))
elif 18.5 <= imc < 25:
    print('Parabéns, {}! Você está no peso ideal para a sua altura.'.format(nome))
elif 25 <= imc < 30:
    print('Tome cuidado, {}! Você está com sobrepeso.'.format(nome))
elif 30 <= imc < 40:
    print('Procure ajuda médica, {}! Você está obeso.'.format(nome))
else:
    print('Procure ajuda médica urgentemente, {}! Você está com obesidade mórbida.'.format(nome))
