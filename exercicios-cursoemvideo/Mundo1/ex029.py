# Desafio 029 - Escreva um programa que leia a velocidade de um carro.
# - Se ele ultrapassar 80 km/h, mostre uma mensagem dizendo que ele foi multado.
# - A multa vai custar R$ 7,00 por cada km/h acima do limite

print('Desafio 029 - Radar eletrônico')
velocidadeRegistradaPeloRadar = str(input('\nVelocidade registrada pelo radar (em km/h - somente números): ')).strip()

print('\n', end='')

if not(velocidadeRegistradaPeloRadar.isnumeric()):
    print('Entrada inválida! Reinicie o programa e tente novamente.')
else:
    velocidadeRegistradaPeloRadar = int(velocidadeRegistradaPeloRadar)
    if velocidadeRegistradaPeloRadar > 80:
        multa = (velocidadeRegistradaPeloRadar - 80) * 7
        print('Você foi multado em R${:.2f} por andar acima do limite permitido de 80 km/h.'.format(multa))
    print('Tenha um bom dia! Dirija com segurança!')
