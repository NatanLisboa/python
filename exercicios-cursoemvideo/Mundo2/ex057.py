# Aula 14 - Estrutura de repetição while (Estrutura de repetição com teste lógico)

# Desafio 057 - Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores 'M' ou 'F'. Caso esteja errado,
# peça a digitação novamente até ter um valor correto

print('Desafio 057 - Validação de Dados')
sexo = 'J'
while not(sexo == 'M' or sexo == 'F' or sexo == 'm' or sexo == 'f'):
    sexo = str(input('Digite seu sexo [M/F]: ')).strip()
    if not(sexo == 'M' or sexo == 'F' or sexo == 'm' or sexo == 'f'):
        print('\n\033[4;31mDADO INVÁLIDO INSERIDO! POR FAVOR, DIGITE "M" OU "F".\033[m\n')

print('\n', end='')
if sexo in 'Mm':
    print('Sexo MASCULINO registrado com sucesso!')
else:
    print('Sexo FEMININO registrado com sucesso!')
