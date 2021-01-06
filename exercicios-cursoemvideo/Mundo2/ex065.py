# Aula 14 - Estrutura de repetição while (Estrutura de repetição com teste lógico)

# Desafio 065 - Crie um programa que leia vários números inteiros pelo teclado. No final da execução, mostre a média
# entre todos os valores e qual foi o maior e o menor valor lido. O programa deve perguntar ao usuário se ele quer ou
# não continuar a digitar valores.

print('\nDesafio 065 - Maior e Menor Valores\n')
continuarDigitacao = 'S'
numeroValido = quantidadeNumeros = soma = maior = menor = 0  # Todas essas variáveis recebem 0

while continuarDigitacao in 'Ss':

    numeroValido = 0
    while not numeroValido:
        numero = str(input('Digite um número inteiro: '))
        if numero.isnumeric():
            numeroValido = 1
        elif numero == '':
            print('\n\033[4;31mVOCÊ NÃO DIGITOU UM NÚMERO INTEIRO! TENTE NOVAMENTE.\033[m\n')
        elif numero[0] == '-' and numero[1:].isnumeric():
            numeroValido = 1
        else:
            print('\n\033[4;31mVOCÊ NÃO DIGITOU UM NÚMERO INTEIRO! TENTE NOVAMENTE.\033[m\n')

    quantidadeNumeros += 1
    soma += int(numero)
    if quantidadeNumeros == 1:
        maior = menor = int(numero)
    elif int(numero) > maior:
        maior = int(numero)
    elif int(numero) < menor:
        menor = int(numero)

    continuarDigitacao = 'r'
    while not((continuarDigitacao == 'S') or (continuarDigitacao == 'N') or (continuarDigitacao == 's') or
              (continuarDigitacao == 'n')):
        continuarDigitacao = str(input('Deseja digitar mais números para a soma? [S/N]: '))
        if not((continuarDigitacao == 'S') or (continuarDigitacao == 'N') or (continuarDigitacao == 's') or
               (continuarDigitacao == 'n')):
            print('\n\033[4;31mRESPOSTA INVÁLIDA! DIGITE "S" OU "N"\033[m\n')

print('\n')
if quantidadeNumeros == 1:
    print('Média do único número digitado: {}'.format(soma / quantidadeNumeros))
else:
    print('Média entre os {} números digitados: {}'.format(quantidadeNumeros, soma / quantidadeNumeros))
print('Maior número digitado: {}'.format(maior))
print('Menor número digitado: {}'.format(menor))
