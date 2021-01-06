# Aula 14 - Estrutura de repetição while (Estrutura de repetição com teste lógico)

# Exercício Python 69: Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada, o
# programa deverá perguntar se o usuário quer ou não continuar. No final, mostre:
# A) quantas pessoas tem mais de 18 anos.
# B) quantos homens foram cadastrados.
# C) quantas mulheres tem menos de 20 anos.

pessoasComMaisDe18Anos = quantidadeHomensCadastrados = mulheresComMenosDe20Anos = 0

print('\nDesafio 069 - Análise de dados do grupo\n')

while True:

    while True:
        idade = str(input('Digite a sua idade: ')).strip()
        if idade.isnumeric():
            idade = int(idade)
            break
        else:
            print('\n\033[31mIDADE INVÁLIDA INSERIDA! POR FAVOR, DIGITE UM NÚMERO INTEIRO POSITIVO!\033[m\n')

    while True:
        sexo = str(input('Informe o seu sexo [M/F]: ')).strip().upper()
        if sexo == 'M' or sexo == 'F':
            break
        else:
            print('\n\033[31mENTRADA INVÁLIDA INSERIDA! POR FAVOR, DIGITE "M" OU "F"\033[m\n')

    if idade > 18:
        pessoasComMaisDe18Anos += 1
    if sexo == 'M':
        quantidadeHomensCadastrados += 1
    elif idade < 20:
        mulheresComMenosDe20Anos += 1

    while True:
        continuarInsercao = str(input('Deseja cadastrar outro registro [S/N]: ')).strip().upper()
        if continuarInsercao == 'S' or continuarInsercao == 'N':
            break
        else:
            print('\n\033[31mENTRADA INVÁLIDA INSERIDA! POR FAVOR, DIGITE "S" OU "N"\033[m\n')

    if continuarInsercao == 'N':
        break

print(f'\n\nQuantidade de pessoas com mais de 18 anos cadastradas: {pessoasComMaisDe18Anos}')
print(f'Quantidade de homens cadastrados: {quantidadeHomensCadastrados}')
print(f'Quantidade de mulheres com menos de 20 anos cadastradas: {mulheresComMenosDe20Anos}')
