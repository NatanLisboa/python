# Aula 14 - Estrutura de repetição while (Estrutura de repetição com teste lógico)

# Desafio 061 - Refaça o DESAFIO 051, lendo o primeiro termo e a razão de uma PA, mostrando os 10 primeiros termos da
# progessão usando a estrutura while.

print('\nDesafio 062 - Super Progressão Aritmética v3.0\n')

numeroValido = 0

while numeroValido < 2:
    numeroValido = 0
    a1 = str(input('Primeiro termo da PA: ')).strip()
    r = str(input('Razão da PA: ')).strip()
    if a1.isnumeric():
        numeroValido += 1
    elif a1[0] == '-' and a1[1:].isnumeric():
        numeroValido += 1
    elif a1[0] == '-' and a1[1:a1.find('.')].isnumeric() and a1[(a1.find('.') + 1):].isnumeric():
        numeroValido += 1
    elif a1[0] == '-' and a1[1:a1.find('.')].isnumeric() and len(a1) == a1.find('.') + 1:
        numeroValido += 1
    elif a1[:a1.find('.')].isnumeric() and a1[(a1.find('.') + 1):].isnumeric():
        numeroValido += 1
    elif a1[:a1.find('.')].isnumeric() and len(a1) == a1.find('.') + 1:
        numeroValido += 1
    else:
        print('\033[4;31mVOCÊ DIGITOU UM VALOR INVÁLIDO PARA O 1º TERMO DA PA. TENTE NOVAMENTE.\033[m\n')
    if numeroValido == 1:
        if r.isnumeric():
            numeroValido += 1
        elif r[0] == '-' and r[1:].isnumeric():
            numeroValido += 1
        elif r[0] == '-' and r[1:r.find('.')].isnumeric() and r[(r.find('.') + 1):].isnumeric():
            numeroValido += 1
        elif r[0] == '-' and r[1:r.find('.')].isnumeric() and len(r) == r.find('.') + 1:
            numeroValido += 1
        elif r[:r.find('.')].isnumeric() and r[(r.find('.') + 1):].isnumeric():
            numeroValido += 1
        elif r[:r.find('.')].isnumeric() and len(r) == r.find('.') + 1:
            numeroValido += 1
        else:
            print('\033[4;31mVOCÊ DIGITOU UM VALOR INVÁLIDO PARA A RAZÃO DA PA. TENTE NOVAMENTE.\033[m\n')

a1 = float(a1)
r = float(r)
an = a1
i = 1

print('\nProgressão aritmética: ', end='')
while i < 11:
    print('{}'.format(an), end=' ')
    an += r
    i += 1

maisTermos = '1'
while int(maisTermos) > 0:
    maisTermos = str(input('\n\nQuantos outros termos a partir do último você deseja ver (Digite 0 para encerrar): '))
    if maisTermos.isnumeric() and int(maisTermos) > 0:
        print('\nContinuação da PA:', end=' ')
        auxI = i
        while i < (auxI + int(maisTermos)):
            print('{}'.format(an), end=' ')
            an += r
            i += 1
    elif not(maisTermos.isnumeric()):
        print('\n\033[4;31mVOCÊ DIGITOU UMA LETRA OU UM NÚMERO NEGATIVO. TENTE NOVAMENTE.\033[m')
        maisTermos = '1'
    else:
        print('\nObrigado por utilizar o programa :)')
