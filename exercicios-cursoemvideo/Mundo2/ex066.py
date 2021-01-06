# Aula 14 - Estrutura de repetição while (Estrutura de repetição com teste lógico)

# Desafio 066 - Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando o usuário
# digitar 999, que é a condição de parada. No final, mostre quantos números foram digitados e qual foi a soma entre eles
# (desconsiderando o flag).

soma = quantidadeNumeros = 0
print('\nDesafio 066 - Vários números com flag\n')
while True:
    num = str(input('Digite um número inteiro [999 para parar o programa e mostrar a soma dos números digitados]: '))
    if num.isnumeric() and int(num) != 999:
        quantidadeNumeros += 1
        soma += int(num)
    elif not(num.isnumeric()):
        if num == '' or not(num[0] == '-' and num[1:].isnumeric()):
            print('\n\033[4;31mVOCÊ NÃO DIGITOU UM NÚMERO INTEIRO! TENTE NOVAMENTE.\033[m\n')
        else:
            quantidadeNumeros += 1
            soma += int(num)
    else:
        break

print('\n\n', end='')
if quantidadeNumeros > 1:
    print(f'Soma entre os {quantidadeNumeros} números digitados: {soma}')
elif quantidadeNumeros == 1:
    print(f'Único número digitado: {soma}')
else:
    print('NÃO FOI DIGITADO NENHUM NÚMERO PARA A SOMA.')
