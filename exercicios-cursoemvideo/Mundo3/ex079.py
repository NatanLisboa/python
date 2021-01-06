# Mundo 3 - Aula 17 - Variáveis Compostas - Listas

# Exercício Python 079: Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma
# lista. Caso o número já exista lá dentro, ele não será adicionado. No final, serão exibidos todos os valores únicos
# digitados, em ordem crescente.

print('\nExercício 79 – Valores únicos em uma Lista\n')

listaNumeros = []

while True:
    
    while True:
        num = str(input('Digite um número: ')).strip()
        if num == '':
            print('\n\033[31mVALOR INVÁLIDO INSERIDO! POR FAVOR, DIGITE UM NÚMERO VÁLIDO.\033[m\n')
        elif (num.isnumeric()) or\
                (num[0] == '-' and num[1:].isnumeric()) or\
                (num[0] == '-' and num[1:num.find('.')].isnumeric() and len(num) == num.find('.') + 1) or\
                (num[0] == '-' and num[1:num.find('.')].isnumeric() and num[num.find('.') + 1:].isnumeric()) or\
                (num[0:num.find('.')].isnumeric() and len(num) == num.find('.') + 1) or\
                (num[0:num.find('.')].isnumeric() and num[num.find('.') + 1:].isnumeric()):
            num = float(num)
            print('\n', end='')
            if num not in listaNumeros:
                listaNumeros.append(num)
                print('\n\033[34mNÚMERO ADICIONADO NA LISTA COM SUCESSO!\033[m\n')
                break
            else:
                print('\n\033[31mESSE NÚMERO JÁ EXISTE NA LISTA! POR FAVOR, DIGITE OUTRO.\033[m\n')
        else:
            print('\n\033[31mVALOR INVÁLIDO INSERIDO! POR FAVOR, DIGITE UM NÚMERO VÁLIDO.\033[m\n')

    while True:
        continuarDigitacao = str(input('Deseja digitar outro número? (S/N): ')).strip().upper()
        if continuarDigitacao == 'S' or continuarDigitacao == 'N':
            break
        else:
            print('\n\033[31mRESPOSTA INVÁLIDA! POR FAVOR, DIGITE "S" OU "N"\033[m\n')

    print('\n', end='')

    if continuarDigitacao == 'N':
        break


print(f'Lista original: {listaNumeros}')
listaNumeros.sort()
print(f'Lista em ordem crescente: {listaNumeros}')
