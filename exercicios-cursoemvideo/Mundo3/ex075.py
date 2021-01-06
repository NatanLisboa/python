# Mundo 3 - Aula 16 - Variáveis Compostas - Tuplas

# Exercício Python 075: Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla.
# No final, mostre:
#
# A) Quantas vezes apareceu o valor 9.
#
# B) Em que posição foi digitado o primeiro valor 3.
#
# C) Quais foram os números pares.

print('\nExercício 75 – Análise de dados em uma Tupla\n')

while True:

    while True:
        num1 = str(input('1º número inteiro: ')).strip()
        if not((num1.isnumeric()) or (num1[0] == '-' and num1[1:].isnumeric())):
            print('\n\033[31mVALOR INVÁLIDO! POR FAVOR, DIGITE UM NÚMERO INTEIRO\033[m\n')
        else:
            num1 = int(num1)
            break

    while True:
        num2 = str(input('2º número inteiro: ')).strip()
        if not((num2.isnumeric()) or (num2[0] == '-' and num2[1:].isnumeric())):
            print('\n\033[31mVALOR INVÁLIDO! POR FAVOR, DIGITE UM NÚMERO INTEIRO\033[m\n')
        else:
            num2 = int(num2)
            break

    while True:
        num3 = str(input('3º número inteiro: ')).strip()
        if not ((num3.isnumeric()) or (num3[0] == '-' and num3[1:].isnumeric())):
            print('\n\033[31mVALOR INVÁLIDO! POR FAVOR, DIGITE UM NÚMERO INTEIRO\033[m\n')
        else:
            num3 = int(num3)
            break

    while True:
        num4 = str(input('4º número inteiro: ')).strip()
        if not ((num4.isnumeric()) or (num4[0] == '-' and num4[1:].isnumeric())):
            print('\n\033[31mVALOR INVÁLIDO! POR FAVOR, DIGITE UM NÚMERO INTEIRO\033[m\n')
        else:
            num4 = int(num4)
            break

    tuplaNumeros = (num1, num2, num3, num4)

    print(f'\n\nNúmeros digitados: {tuplaNumeros}')
    print(f'\nOcorrências do número 9: {tuplaNumeros.count(9)}')
    if 3 in tuplaNumeros:
        print(f'Posição da primeira ocorrência do valor 3: {tuplaNumeros.index(3) + 1}ª posição')
    else:
        print('Posição da primeira ocorrência do valor 3: Não há ocorrências')
    print('Números pares digitados: ', end='')
    for num in tuplaNumeros:
        if num % 2 == 0:
            print(num, end='  ')

    print('\n')

    while True:
        continuarPrograma = str(input('Deseja digitar mais números? (S/N): ')).strip().upper()
        if continuarPrograma == 'S' or continuarPrograma == 'N':
            break
        else:
            print('\n\033[31mRESPOSTA INVÁLIDA! POR FAVOR, DIGITE "S" OU "N"\033[m\n')

    if continuarPrograma == 'N':
        break

    print('\n')

print('\nObrigado por utilizar o programa :)')
