# Aula 14 - Estrutura de repetição while (Estrutura de repetição com teste lógico)

# Desafio 064 - Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando o usuário
# digitar 999, que é a condição de parada. No final, mostre quantos números foram digitados e qual foi a soma entre eles
# (desconsiderando o flag)

print('\nDesafio 064 - Tratando vários valores v1.0\n')

num = '-1'
soma = quantidadeNumeros = 0

while int(num) != 999:
    num = str(input('''Digite um número inteiro (Digite 999 para mostrar a soma entre os números 
digitados, exceto o 999): '''))
    print('\n\n', end='')
    if not(num.isnumeric()):
        if num == '':
            print('\033[4;31mVOCÊ NÃO DIGITOU UM NÚMERO INTEIRO! TENTE NOVAMENTE.\033[m')
            num = '-1'
            print('\n', end='')
        elif not((num[0] == '-') and (num[1:].isnumeric())):
            print('\033[4;31mVOCÊ NÃO DIGITOU UM NÚMERO INTEIRO! TENTE NOVAMENTE.\033[m')
            num = '-1'
            print('\n', end='')
        elif int(num) != 999:
            quantidadeNumeros += 1
            soma += int(num)
    elif int(num) != 999:
        quantidadeNumeros += 1
        soma += int(num)

print('\n')
if quantidadeNumeros == 0:
    print('VOCÊ NÃO DIGITOU NENHUM NÚMERO PARA A SOMA.')
elif quantidadeNumeros == 1:
    print('Único valor digitado: {}'.format(soma))
else:
    print('Soma entre os {} valores digitados: {}'.format(quantidadeNumeros, soma))
