# Aula 14 - Estrutura de repetição while (Estrutura de repetição com teste lógico)

# Exercício Python 071: Crie um programa que simule o funcionamento de um caixa eletrônico. No início, pergunte ao
# usuário qual será o valor a ser sacado (número inteiro) e o programa vai informar quantas cédulas de cada valor serão
# entregues. OBS:

# considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1.

cedulas50 = cedulas20 = cedulas10 = cedulas1 = 0

print('\nDesafio 071 – Simulador de Caixa Eletrônico\n')
while True:

    while True:
        valorASerSacado = str(input('Valor a ser sacado: R$'))
        if not valorASerSacado.isnumeric():
            print('\n\033[31mVALOR INVÁLIDO INSERIDO! POR FAVOR, DIGITE UM VALOR INTEIRO POSITIVO.\033[m\n')
        else:
            valorASerSacado = int(valorASerSacado)
            valorRestanteASerSacado = int(valorASerSacado)
            break

    while True:
        if valorRestanteASerSacado == 0:
            break
        else:
            while valorRestanteASerSacado != 0:
                if valorRestanteASerSacado // 50 > 0:
                    valorRestanteASerSacado -= 50
                    cedulas50 += 1
                elif valorRestanteASerSacado // 20 > 0:
                    valorRestanteASerSacado -= 20
                    cedulas20 += 1
                elif valorRestanteASerSacado // 10 > 0:
                    valorRestanteASerSacado -= 10
                    cedulas10 += 1
                elif valorRestanteASerSacado // 1 > 0:
                    valorRestanteASerSacado -= 1
                    cedulas1 += 1

    if valorRestanteASerSacado == 0:
        break

if int(valorASerSacado) > 0:
    print(f'\nVocê receberá os R${valorASerSacado:.2f} em: ')
    if cedulas50 > 0:
        print(f'{cedulas50} cédulas de R$50' if cedulas50 > 1 else '1 cédula de R$50')
    if cedulas20 > 0:
        print(f'{cedulas20} cédulas de R$20' if cedulas20 > 1 else '1 cédula de R$20')
    if cedulas10 > 0:
        print(f'{cedulas10} cédulas de R$10' if cedulas10 > 1 else '1 cédula de R$10')
    if cedulas1 > 0:
        print(f'{cedulas1} cédulas de R$1' if cedulas1 > 1 else '1 cédula de R$1')

print('\nAgradecemos a preferência!')
