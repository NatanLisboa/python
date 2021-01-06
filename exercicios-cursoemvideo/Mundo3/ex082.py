# Mundo 3 - Aula 17 - Variáveis Compostas - Listas

# Exercício Python 082: Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, crie duas
# listas extras que vão conter apenas os valores pares e os valores ímpares digitados, respectivamente. Ao final, mostre
# o conteúdo das três listas geradas.

listaNumeros = []

print('\nExercício 82 – Dividindo valores em várias listas\n')

while True:

    while True:
        numeroDigitado = str(input('Digite um número inteiro: ')).strip()
        if numeroDigitado.isnumeric() or (numeroDigitado[0] == '-' and numeroDigitado[1:].isnumeric()):
            numeroDigitado = int(numeroDigitado)
            listaNumeros.append(numeroDigitado)
            break
        else:
            print('\n\033[31mVALOR INVÁLIDO DIGITADO! POR FAVOR, DIGITE UM NÚMERO INTEIRO.\033[m\n')

    while True:
        continuarDigitacao = str(input('Deseja digitar outro número? (S/N): ')).strip().upper()
        if continuarDigitacao == 'S' or continuarDigitacao == 'N':
            break
        else:
            print('\n\033[31mRESPOSTA INVÁLIDA! POR FAVOR, DIGITE "S" OU "N"\033[m\n')

    if continuarDigitacao == 'N':
        break


listaNumerosPares = []
listaNumerosImpares = []

for numero in listaNumeros:
    if numero % 2 == 0:
        listaNumerosPares.append(numero)
    else:
        listaNumerosImpares.append(numero)

print(f'\n\nLista dos números digitados: {listaNumeros}')
print(f'Lista dos números pares digitados: {listaNumerosPares}')
print(f'Lista dos números ímpares digitados: {listaNumerosImpares}')
