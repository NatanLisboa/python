# Aula 14 - Estrutura de repetição while (Estrutura de repetição com teste lógico)

# Desafio 059 - Crie um programa que leia dois valores e mostre um menu na tela:
# [1] - Somar
# [2] - Multiplicar
# [3] - Maior
# [4] - Novos números
# [5] - Sair do programa

from time import sleep

print('\nDesafio 059 - Criando um Menu de Opções\n')

opcao = '-1'
numeroValido = 0

while numeroValido < 2:
    numeroValido = 0
    n1 = str(input('Digite o 1º valor: ')).strip()
    n2 = str(input('Digite o 2º valor: ')).strip()
    if n1.isnumeric():
        numeroValido += 1
    elif n1 == '':
        print('\033[4;31mVOCÊ DIGITOU UM VALOR INVÁLIDO NO 1º NÚMERO. TENTE NOVAMENTE.\033[m\n')
    elif n1[0] == '-' and n1[1:].isnumeric():
        numeroValido += 1
    elif n1[0] == '-' and n1[1:n1.find('.')].isnumeric() and n1[(n1.find('.') + 1):].isnumeric():
        numeroValido += 1
    elif n1[0] == '-' and n1[1:n1.find('.')].isnumeric() and len(n1) == n1.find('.') + 1:
        numeroValido += 1
    elif n1[:n1.find('.')].isnumeric() and n1[(n1.find('.') + 1):].isnumeric():
        numeroValido += 1
    elif n1[:n1.find('.')].isnumeric() and len(n1) == n1.find('.') + 1:
        numeroValido += 1
    else:
        print('\033[4;31mVOCÊ DIGITOU UM VALOR INVÁLIDO NO 1º NÚMERO. TENTE NOVAMENTE.\033[m\n')
    if numeroValido == 1:
        if n2.isnumeric():
            numeroValido += 1
        elif n2 == '':
            print('\033[4;31mVOCÊ DIGITOU UM VALOR INVÁLIDO NO 2º NÚMERO. TENTE NOVAMENTE.\033[m\n')
        elif n2[0] == '-' and n2[1:].isnumeric():
            numeroValido += 1
        elif n2[0] == '-' and n2[1:n2.find('.')].isnumeric() and n2[(n2.find('.') + 1):].isnumeric():
            numeroValido += 1
        elif n2[0] == '-' and n2[1:n2.find('.')].isnumeric() and len(n2) == n2.find('.') + 1:
            numeroValido += 1
        elif n2[:n2.find('.')].isnumeric() and n2[(n2.find('.') + 1):].isnumeric():
            numeroValido += 1
        elif n2[:n2.find('.')].isnumeric() and len(n2) == n2.find('.') + 1:
            numeroValido += 1
        else:
            print('\033[4;31mVOCÊ DIGITOU UM VALOR INVÁLIDO NO 2º NÚMERO. TENTE NOVAMENTE.\033[m\n')

while opcao != '5':
    n1 = float(n1)
    n2 = float(n2)
    print('\n' + ('-' * 20) + 'MENU DE OPÇÕES' + ('-' * 20))
    print('\n1º número: {}'.format(n1))
    print('2º número: {}'.format(n2))
    print('''\n[1] - Somar
[2] - Multiplicar
[3] - Maior
[4] - Novos números
[5] - Sair do programa''')
    opcao = str(input('\nEscolha uma opção entre 1 e 5: '))

    print('\n', end='')
    if not(opcao.isnumeric()):
        print('\033[4;31mVOCÊ NÃO DIGITOU UM NÚMERO INTEIRO ENTRE 1 E 5. TENTE NOVAMENTE.\033[m')
        sleep(3)
    elif int(opcao) == 0:
        print('\033[4;31m0 NÃO ESTÁ ENTRE 1 E 5! TENTE NOVAMENTE.\033[m')
        sleep(3)
    elif int(opcao) > 5:
        print('\033[4;31mVOCÊ DIGITOU UM NÚMERO MAIOR QUE 5! TENTE NOVAMENTE.\033[m')
        sleep(3)
    else:
        if opcao == '1':
            print('{} + {} = {}'.format(n1, n2, n1 + n2))
            sleep(3)
        elif opcao == '2':
            print('{} * {} = {}'.format(n1, n2, n1 * n2))
            sleep(3)
        elif opcao == '3':
            if n1 > n2:
                print('O primeiro valor é maior ({} > {})'.format(n1, n2))
            elif n2 > n1:
                print('O segundo valor é maior ({} < {})'.format(n1, n2))
            else:
                print('Os dois valores são iguais ({} = {})'.format(n1, n2))
            sleep(3)
        elif opcao == '4':
            numeroValido = 0
            while numeroValido < 2:
                numeroValido = 0
                n1 = str(input('Digite o 1º valor: ')).strip()
                n2 = str(input('Digite o 2º valor: ')).strip()
                if n1.isnumeric():
                    numeroValido += 1
                elif n1 == '':
                    print('\033[4;31mVOCÊ DIGITOU UM VALOR INVÁLIDO NO 1º NÚMERO. TENTE NOVAMENTE.\033[m\n')
                elif n1[0] == '-' and n1[1:].isnumeric():
                    numeroValido += 1
                elif n1[0] == '-' and n1[1:n1.find('.')].isnumeric() and n1[(n1.find('.') + 1):].isnumeric():
                    numeroValido += 1
                elif n1[0] == '-' and n1[1:n1.find('.')].isnumeric() and len(n1) == n1.find('.') + 1:
                    numeroValido += 1
                elif n1[:n1.find('.')].isnumeric() and n1[(n1.find('.') + 1):].isnumeric():
                    numeroValido += 1
                elif n1[:n1.find('.')].isnumeric() and len(n1) == n1.find('.') + 1:
                    numeroValido += 1
                else:
                    print('\033[4;31mVOCÊ DIGITOU UM VALOR INVÁLIDO NO 1º NÚMERO. TENTE NOVAMENTE.\033[m\n')
                    sleep(3)
                if numeroValido == 1:
                    if n2.isnumeric():
                        numeroValido += 1
                    elif n2 == '':
                        print('\033[4;31mVOCÊ DIGITOU UM VALOR INVÁLIDO NO 2º NÚMERO. TENTE NOVAMENTE.\033[m\n')
                    elif n2[0] == '-' and n2[1:].isnumeric():
                        numeroValido += 1
                    elif n2[0] == '-' and n2[1:n2.find('.')].isnumeric() and n2[(n2.find('.') + 1):].isnumeric():
                        numeroValido += 1
                    elif n2[0] == '-' and n2[1:n2.find('.')].isnumeric() and len(n2) == n2.find('.') + 1:
                        numeroValido += 1
                    elif n2[:n2.find('.')].isnumeric() and n2[(n2.find('.') + 1):].isnumeric():
                        numeroValido += 1
                    elif n2[:n2.find('.')].isnumeric() and len(n2) == n2.find('.') + 1:
                        numeroValido += 1
                    else:
                        print('\033[4;31mVOCÊ DIGITOU UM VALOR INVÁLIDO NO 2º NÚMERO. TENTE NOVAMENTE.\033[m\n')
                        sleep(3)
        else:
            print('Obrigado por utilizar o programa!')
