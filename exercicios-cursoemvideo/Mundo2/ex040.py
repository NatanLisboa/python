# Mundo 2 - Aula 12 - Condições Aninhadas

# Desafio 040 - Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final,
# de acordo com a média atingida

# - Média abaixo de 5.0: REPROVADO
# - Média entre 5.0 e 6.9: RECUPERAÇÃO
# - Média 7.0 ou superior: APROVADO

print('\nDesafio 040 - Aquele clássico da Média\n')
n1 = float(input('1ª nota do aluno: '))
n2 = float(input('2ª nota do aluno: '))

media = (n1 + n2) / 2

print('\nAluno ', end='')
if media < 5.0:
    print('\033[31mREPROVADO\033[m ', end='')
elif 5.0 <= media <= 6.9:
    print('de \033[33mRECUPERAÇÃO\033[m ', end='')
else:
    print('\033[34mAPROVADO\033[m ', end='')
print('com média {}'.format(media))
