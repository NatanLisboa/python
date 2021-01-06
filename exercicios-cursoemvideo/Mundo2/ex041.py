# Mundo 2 - Aula 12 - Condições Aninhadas

# Desafio 041 - A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta e
# mostre sua categoria, de acordo com sua idade:

# Até 9 anos: MIRIM
# Até 14 anos: INFANTIL
# Até 19 anos: JÚNIOR
# Até 20 anos: SÊNIOR
# Acima: MASTER

from datetime import date

print('\nDesafio 041 - Classificando Atletas\n')
anoAtual = date.today().year
anoNascimento = str(input('Digite o ano de nascimento do atleta: '))

if not(anoNascimento.isnumeric()):
    print('Ano inválido digitado!')
else:
    idade = anoAtual - int(anoNascimento)
    if idade < 0:
        print('Esse atleta pertencerá à categoria MIRIM assim que nascer.')
    elif 0 <= idade <= 9:
        print('Esse atleta pertence à categoria MIRIM.')
    elif 10 <= idade <= 14:
        print('Esse atleta pertence à categoria INFANTIL.')
    elif 15 <= idade <= 19:
        print('Esse atleta pertence à categoria JUNIOR.')
    elif 20 <= idade <= 25:
        print('Esse atleta pertence à categoria SÊNIOR.')
    else:
        print('Esse atleta pertence à categoria MASTER.')
