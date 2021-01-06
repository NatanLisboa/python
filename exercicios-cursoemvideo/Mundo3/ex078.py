# Mundo 3 - Aula 17 - Variáveis Compostas - Listas

# Exercício Python 078: Faça um programa que leia 5 valores numéricos e guarde-os em uma lista. No final, mostre qual
# foi o maior e o menor valor digitado e as suas respectivas posições na lista.

valores = list()
indicesMaiorValor = list()
indicesMenorValor = list()
i = 0

print('\nExercício 78 – Maior e Menor valores na Lista\n')
while True:

    if i == 5:
        break

    print(f'Valores na lista: {valores}\n')

    num = str(input(f'{i + 1}º número: ')).strip()
    if num == '':
        print('\n\033[31mVALOR INVÁLIDO DIGITADO! POR FAVOR, DIGITE UM NÚMERO VÁLIDO.\033[m\n')
    elif (num.isnumeric()) or\
        (num[0] == '-' and num[1:].isnumeric()) or\
        (num[0] == '-' and num[1:num.find('.')].isnumeric() and num[num.find('.') + 1:].isnumeric()) or\
        (num[0] == '-' and num[1:num.find('.')].isnumeric() and len(num) == num.find('.') + 1) or\
        (num[0:num.find('.')].isnumeric() and num[num.find('.') + 1:].isnumeric()) or\
            (num[0:num.find('.')].isnumeric() and len(num) == num.find('.') + 1):
        valores.append(float(num))
        i += 1
    else:
        print('\n\033[31mVALOR INVÁLIDO DIGITADO! POR FAVOR, DIGITE UM NÚMERO VÁLIDO.\033[m\n')

for i in range(0, len(valores)):
    if valores[i] == max(valores):
        indicesMaiorValor.append(i)
    if valores[i] == min(valores):
        indicesMenorValor.append(i)

print(f'\nValores digitados: {valores}')
print(f'O maior valor digitado está na ', end='')

for i in range(0, len(indicesMaiorValor)):
    if i == len(indicesMaiorValor) - 1 and len(indicesMaiorValor) > 1:
        print(' e ', end='')
    elif 1 <= i < len(indicesMaiorValor):
        print(', ', end='')
    print(f'{indicesMaiorValor[i] + 1}ª', end='')

print(f' posição da lista e é o {max(valores)}')

print(f'O menor valor digitado está na ', end='')

for i in range(0, len(indicesMenorValor)):
    if i == len(indicesMenorValor) - 1 and len(indicesMenorValor) > 1:
        print(' e ', end='')
    elif 1 <= i < len(indicesMenorValor):
        print(', ', end='')
    print(f'{indicesMenorValor[i] + 1}ª', end='')

print(f' posição da lista e é o {min(valores)}')
