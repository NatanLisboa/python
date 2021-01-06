# Aula 13 - Estrutura de repetição for

# Desafio 056 - Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa, mostre:
# - A média de idade do grupo
# - Qual o nome do homem mais velho
# - Quantas mulheres têm menos de 21 anos

somaIdades = 0.0
mulheresComMenosDe20Anos = 0
nomeHomemMaisVelho = ''
idadeHomemMaisVelho = 0
print('\nDesafio 056 - Analisador Completo')

for i in range(1, 5):
    nome = str(input('\nNome da {}ª pessoa: '.format(i))).strip()
    idade = int(input('Idade de {} (somente números): '.format(nome)))
    sexo = str(input('Sexo de {} (M/F): '.format(nome))).strip()

    somaIdades += idade
    if not((sexo in 'Mm') or (sexo in 'Ff')):
        print('\nEntrada inválida inserida para o campo \"sexo\"! Registro invalidado.')
    elif sexo in 'Mm':
        if i == 1:
            idadeHomemMaisVelho = idade
            nomeHomemMaisVelho = nome
        elif idade > idadeHomemMaisVelho:
            idadeHomemMaisVelho = idade
            nomeHomemMaisVelho = nome
    else:
        if idade < 20:
            mulheresComMenosDe20Anos += 1

print('\n\nMédia de idade do grupo: {:.1f} anos'.format(somaIdades / 4))
print('Nome do HOMEM mais velho: {} ({} anos)'.format(nomeHomemMaisVelho, idadeHomemMaisVelho))
print('Quantidade de MULHERES com menos de 20 anos de idade: {}'.format(mulheresComMenosDe20Anos))
