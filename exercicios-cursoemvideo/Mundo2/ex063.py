# Aula 14 - Estrutura de repetição while (Estrutura de repetição com teste lógico)

# Desafio 063 - Escreva um programa que leia um número n inteiro qualquer e mostre na tela os n primeiros elementos de
# uma sequência de Fibonacci.

print('\nDesafio 063 - Sequência de Fibonacci v1.0\n')

quantidadeTermos = '1'
while int(quantidadeTermos) != 0:

    i = 1
    termoAtual = 0
    termoAnterior = -1
    proximoTermo = 1

    quantidadeTermos = str(input('''Digite a quantidade de termos que você deseja ver da sequência de Fibonacci 
(Digite 0 para encerrar o programa): '''))
    print('\n\n', end='')

    if not(quantidadeTermos.isnumeric()):
        print('\033[4;31mVOCÊ DIGITOU UMA LETRA, UM NÚMERO NEGATIVO OU UM NÚMERO COM VÍRGULA. TENTE NOVAMENTE.\033[m\n')
        quantidadeTermos = '-1'
    elif int(quantidadeTermos) == 0:
        print('OBRIGADO POR UTILIZAR O PROGRAMA :)')
    else:
        print('Sequência de Fibonacci:', end=' ')
        while i <= int(quantidadeTermos):
            print('{}'.format(termoAtual), end=' ')
            termoAnterior = termoAtual
            termoAtual = proximoTermo
            proximoTermo = termoAtual + termoAnterior
            i += 1
    print('\n')
