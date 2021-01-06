# Aula 13 - Estrutura de repetição for

# Desafio 054 - Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas pessoas ainda
# não atingiram a maioridade e quantas já são maiores.

from datetime import date

maioresDeIdade = 0
menoresDeIdade = 0

print('\nDesafio 054 - Grupo da Maioridade\n')

for i in range(1, 8):
    anoNascimento = int(input('Ano de nascimento da {}ª pessoa: '.format(i)))
    if date.today().year - anoNascimento >= 21:
        maioresDeIdade += 1
    else:
        menoresDeIdade += 1

print('\nPessoas menores de idade (menos de 21 anos): {}'.format(menoresDeIdade))
print('Pessoas maiores de idade (21 anos ou mais): {}'.format(maioresDeIdade))
