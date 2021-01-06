# Aula 14 - Estrutura de repetição while (Estrutura de repetição com teste lógico)

# Desafio 067 - Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado pelo
# usuário. O programa será interrompido quando o número solicitado for negativo.

print('-' * 30)
print('Desafio 067 - Tabuada v3.0')
print('-' * 30)

while True:
    num = str(input('Digite um número para ver a sua tabuada (Digite um número negativo para encerrar o programa): '))
    numeroValido = False
    if num.isnumeric():
        numeroValido = True
    elif num[0] == '-' and num[1:num.find('.')].isnumeric() and num[num.find('.') + 1:].isnumeric():
        numeroValido = True
    elif num[0] == '-' and num[1:num.find('.')].isnumeric():
        numeroValido = True
    elif num[0] == '-' and num[1:].isnumeric():
        numeroValido = True
    elif num[:num.find('.')].isnumeric() and len(num) == num.find('.') + 1:
        numeroValido = True
    elif num[:num.find('.')].isnumeric() and num[num.find('.') + 1:].isnumeric():
        numeroValido = True

    if not numeroValido:
        print('\n\033[4;31mVOCÊ NÃO DIGITOU UM NÚMERO VÁLIDO! TENTE NOVAMENTE.\033[m\n')
    else:
        num = float(num)
        if num < 0.0:
            break
        else:
            print('-' * 30)
            for i in range(0, 11):
                print(f'{num} x {i:>2} = {num * i}')
            print('-' * 30)

print('\nObrigado por utilizar o programa :)')