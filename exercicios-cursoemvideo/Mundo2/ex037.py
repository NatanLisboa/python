# Mundo 2 - Aula 12 - Condições Aninhadas

# Desafio 037 - Escreva um programa que leia um número inteiro qualquer e peça para o usuário escolher qual será a base
# de conversão:

# - 1 para binário
# - 2 para octal
# - 3 para hexadecimal

print('\nDesafio 037 - Conversor de Bases Numéricas')
numeroInteiro = int(input('Digite um número inteiro: '))
print('\n1 para binário')
print('2 para octal')
print('3 para hexadecimal')
opcaoEscolhida = int(input('\nSelecione a base de conversão: '))

print('\n')
if opcaoEscolhida == 1:
    numeroInteiroEmBinario = (bin(numeroInteiro))[2:]
    print('{} = {}'.format(numeroInteiro, numeroInteiroEmBinario))

elif opcaoEscolhida == 2:
    numeroInteiroEmOctal = (oct(numeroInteiro))[2:]
    print('{} = {}'.format(numeroInteiro, numeroInteiroEmOctal))

elif opcaoEscolhida == 3:
    numeroInteiroEmHexadecimal = (hex(numeroInteiro))[2:]
    print('{} = {}'.format(numeroInteiro, numeroInteiroEmHexadecimal))

else:
    print('Opção inválida inserida! Reinicie o programa e tente novamente.')
