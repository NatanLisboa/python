# Mundo 3 - Aula 17 - Variáveis Compostas - Listas

# Exercício Python 081: Crie um programa que vai ler vários números e colocar em uma lista.

# Depois disso, mostre:

# A) Quantos números foram digitados.
# B) A lista de valores, ordenada de forma decrescente.
# C) Se o valor 5 foi digitado e está ou não na lista

listaNumeros = []

print('\nExercício 81 – Extraindo dados de uma Lista\n')

while True:

    while True:
        num = str(input('Digite um número: ')).strip()
        if num == '':
            print('\n\033[31mVALOR INVÁLIDO INSERIDO! POR FAVOR, DIGITE UM NÚMERO VÁLIDO.\033[m\n')
        elif (num.isnumeric()) or \
                (num[0] == '-' and num[1:].isnumeric()) or \
                (num[0] == '-' and num[1:num.find('.')].isnumeric() and len(num) == num.find('.') + 1) or \
                (num[0] == '-' and num[1:num.find('.')].isnumeric() and num[num.find('.') + 1:].isnumeric()) or \
                (num[0:num.find('.')].isnumeric() and len(num) == num.find('.') + 1) or \
                (num[0:num.find('.')].isnumeric() and num[num.find('.') + 1:].isnumeric()):
            listaNumeros.append(float(num))
            break
        else:
            print('\n\033[31mVALOR INVÁLIDO INSERIDO! POR FAVOR, DIGITE UM NÚMERO VÁLIDO.\033[m\n')

    while True:
        continuarDigitacao = str(input('Deseja digitar outro número? (S/N): ')).strip().upper()
        if continuarDigitacao == 'S' or continuarDigitacao == 'N':
            break
        else:
            print('\n\033[31mRESPOSTA INVÁLIDA! POR FAVOR, DIGITE "S" OU "N"\033[m\n')

    if continuarDigitacao == 'N':
        break

print(f'\n\nQuantidade de números digitados: {len(listaNumeros)}')
listaNumeros.sort(reverse=True)
print(f'Lista em ordem decrescente: {listaNumeros}')
print('O valor 5 ', end='')
if 5 not in listaNumeros:
    print('NÃO ', end='')
print('foi encontrado na lista')
