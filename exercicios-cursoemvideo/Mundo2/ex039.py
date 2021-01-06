# Mundo 2 - Aula 12 - Condições Aninhadas

# Desafio 039 - Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade:

# - Se ele ainda vai se alistar ao serviço militar.
# - Se é a hora de se alistar.
# - Se já passou do tempo do alistamento.

# Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.

from datetime import date

print('\nDesafio 039 - Alistamento Militar\n')

anoAtual = date.today().year

sexo = str(input('Digite o seu sexo (F/M): '))
print('\n', end='')
if sexo.upper() == 'F':
    print('Você não precisa se alistar. O alistamento militar OBRIGATÓRIO é feito somente por jovens do sexo ', end=''
          'masculino. Seu alistamento é FACULTATIVO.')
elif sexo.upper() == 'M':
    anoNascimento = int(input('Digite o ano de seu nascimento: '))
    idade = anoAtual - anoNascimento

    print('\n')
    if 0 <= idade < 18:
        print('Ainda falta(m) {} ano(s) para seu alistamento militar.'.format(18 - idade))
        print('Seu alistamento será em {}.'.format(anoAtual + (18 - idade)))
    elif idade == 18:
        print('CHEGOU A HORA DE VOCÊ SE ALISTAR!')
    elif idade > 18:
        print('Já se passou(aram) {} ano(s) do prazo para o seu alistamento militar.'.format(idade - 18))
        print('Seu alistamento foi em {}.'.format(anoAtual - (idade - 18)))
    else:
        print('Se preocupe em nascer primeiro, depois pense no alistamento.')
else:
    print('Entrada inválida! Digite F ou M.')

print('\n', end='')
