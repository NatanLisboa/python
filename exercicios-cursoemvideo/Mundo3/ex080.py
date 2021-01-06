# Mundo 3 - Aula 17 - Variáveis Compostas - Listas

# Exercício Python 080: Crie um programa onde o usuário possa digitar cinco valores numéricos e cadastre-os em uma
# lista, já na posição correta de inserção (sem usar o sort()). No final, mostre a lista ordenada na tela.

print('\nExercício 80 – Lista ordenada sem repetições\n')

listaNumeros = []

for i in range(0, 5):
    while True:
        num = str(input(f'{i+1}º número: ')).strip()
        if num == '':
            print('\n\033[31mVALOR INVÁLIDO INSERIDO! POR FAVOR, DIGITE UM NÚMERO VÁLIDO.\033[m\n')
        elif (num.isnumeric()) or \
                (num[0] == '-' and num[1:].isnumeric()) or \
                (num[0] == '-' and num[1:num.find('.')].isnumeric() and len(num) == num.find('.') + 1) or \
                (num[0] == '-' and num[1:num.find('.')].isnumeric() and num[num.find('.') + 1:].isnumeric()) or \
                (num[0:num.find('.')].isnumeric() and len(num) == num.find('.') + 1) or \
                (num[0:num.find('.')].isnumeric() and num[num.find('.') + 1:].isnumeric()):
            num = float(num)
            break
        else:
            print('\n\033[31mVALOR INVÁLIDO INSERIDO! POR FAVOR, DIGITE UM NÚMERO VÁLIDO.\033[m\n')

    if len(listaNumeros) == 0:
        listaNumeros.append(num)
        print(f'Elemento {listaNumeros[0]} adicionado no final da lista')
    else:
        for j in range(0, len(listaNumeros)):
            if num <= listaNumeros[j]:
                break

        if num > listaNumeros[j] and j == len(listaNumeros) - 1:
            listaNumeros.append(num)
            print(f'Elemento {listaNumeros[len(listaNumeros) - 1]} adicionado no final da lista')
        else:
            listaNumeros.insert(j, num)
            print(f'Elemento {listaNumeros[j]} adicionado na posição {j} da lista')

print(f'\n\nLista em ordem crescente: {listaNumeros}')
