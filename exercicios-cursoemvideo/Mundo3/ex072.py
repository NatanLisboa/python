# Mundo 3 - Aula 16 - Variáveis Compostas - Tuplas

# Exercício Python 72: Crie um programa que tenha uma dupla totalmente preenchida com uma contagem por extenso, de zero
# até vinte. Seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso.

numeros = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze',
           'treze', 'catorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')

print('\nExercício 72 – Número por Extenso\n')
while True:

    while True:
        numeroDigitado = str(input('Digite um número entre 0 e 20: ')).strip()
        if numeroDigitado.isnumeric() and 0 <= int(numeroDigitado) <= 20:
            numeroDigitado = int(numeroDigitado)
            break
        print('\n\033[31mVALOR INVÁLIDO INSERIDO! POR FAVOR, INSIRA UM VALOR INTEIRO ENTRE 0 E 20\033[m\n')

    print(f'\n\"{numeroDigitado}\" escrito por extenso é \"{numeros[numeroDigitado]}\"\n')

    while True:
        continuarDigitacao = str(input('Deseja digitar outro número? (S/N): ')).strip().upper()
        if continuarDigitacao == 'S' or continuarDigitacao == 'N':
            break
        else:
            print('\n\033[31mRESPOSTA INVÁLIDA. POR FAVOR, DIGITE "S" OU "N"\033[m\n')

    print('\n')

    if continuarDigitacao == 'N':
        break


print('\nObrigado por utilizar o programa :)\n')
