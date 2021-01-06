# Mundo 3 - Aula 17 - Variáveis Compostas - Listas

# Exercício Python 083: Crie um programa onde o usuário digite uma expressão qualquer que use parênteses. Seu aplicativo
# deverá analisar se a expressão passada está com os parênteses abertos e fechados na ordem correta.

print('\nExercício 83 – Validando expressões matemáticas\n')
operadoresAritmeticos = ('+', '-', '*', '/', '**', '//', '%')
quantidadeOperadoresAritmeticos = 0
quantidadeOperadoresAritmeticosConsecutivos = 0

'''
while True:

    quantidadeOperadoresAritmeticos = 0
    quantidadeOperadoresAritmeticosConsecutivos = 0
    operadorAritmeticoNoInicio = False

    expressaoMatematica = str(input('Digite uma expressão matemática qualquer: ')).strip()

    for i in range(0, len(expressaoMatematica)):
        if expressaoMatematica[i] in operadoresAritmeticos:
            quantidadeOperadoresAritmeticos += 1

    for i in range(0, len(expressaoMatematica.replace(' ', '').replace('(', '').replace(')', ''))):
        if (expressaoMatematica.replace(' ', '').replace('(', '').replace(')', ''))[i].isalnum():
            quantidadeOperadoresAritmeticosConsecutivos = 0
        else:
            quantidadeOperadoresAritmeticosConsecutivos += 1
        if quantidadeOperadoresAritmeticosConsecutivos == 2:
            if (((expressaoMatematica.replace(' ', '').replace('(', '').replace(')', ''))[i-1:i]) == '//' or
                    ((expressaoMatematica.replace(' ', '').replace('(', '').replace(')', ''))[i-1:i]) == '**') and\
                    (((expressaoMatematica.replace(' ', '').replace('(', '').replace(')', ''))[i-2]).isalnum()) and \
                    (((expressaoMatematica.replace(' ', '').replace('(', '').replace(')', ''))[i+1]) not in
                     operadoresAritmeticos):
                quantidadeOperadoresAritmeticosConsecutivos = 0
            else:
                break

    if expressaoMatematica[0] in operadoresAritmeticos and not expressaoMatematica[0] == '-':
        operadorAritmeticoNoInicio = True

    if (expressaoMatematica.count('(') - expressaoMatematica.count(')') == 0) and \
            (quantidadeOperadoresAritmeticos > 0) and (quantidadeOperadoresAritmeticosConsecutivos == 0) and \
            (expressaoMatematica[len(expressaoMatematica) - 1] == ')'
             or (expressaoMatematica.replace(' ', '')[len(expressaoMatematica.replace(' ', '')) - 2] in '+-*/%' and
                 (expressaoMatematica[len(expressaoMatematica) - 1].replace(' ', '')).isalnum())) and\
            not operadorAritmeticoNoInicio:
        print('\n\033[34mEXPRESSÃO VÁLIDA\033[m\n')
    else:
        print('\n\033[31mEXPRESSÃO INVÁLIDA\033[m\n')

    while True:
        continuarDigitacao = str(input('Deseja digitar outra expressão? (S/N): ')).strip().upper()
        if continuarDigitacao == 'S' or continuarDigitacao == 'N':
            break
        else:
            print('\n\033[31mRESPOSTA INVÁLIDA! POR FAVOR, DIGITE "S" OU "N"\033[m\n')

    print('\n')

    if continuarDigitacao == 'N':
        break

'''

expressao = str(input('Digite a expressão: '))
pilha = []
for caractere in expressao:
    if caractere == '(':
        pilha.append('(')
    elif caractere == ')':
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append(')')
            break

print('\n')
if len(pilha) == 0:
    print('\033[34mEXPRESSÃO VÁLIDA!')
else:
    print('\033[31mEXPRESSÃO INVÁLIDA!')
print('\033[m')
