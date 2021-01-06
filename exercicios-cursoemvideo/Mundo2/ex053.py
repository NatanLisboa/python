# Aula 13 - Estrutura de repetição for

# Desafio 053 - Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços.

congruencias = 0
print('\nDesafio 053 - Detector de Palíndromo\n')

# Algoritmo 1
'''
frase = str(input('Digite uma frase: '))
j = len(frase.strip().replace(' ', '')) - 1

print('\n')

if len(frase.strip().replace(' ', '')) % 2 == 0:
    for i in range(0, (len(frase.strip().replace(' ', '')) // 2)):
        if (frase.upper().strip().replace(' ', ''))[i] == (frase.upper().strip().replace(' ', ''))[j]:
            congruencias += 2
        else:
            break
        j -= 1
else:
    for i in range(0, len(frase.strip().replace(' ', '')) // 2 + 1):
        if (frase.upper().strip().replace(' ', ''))[i] == (frase.upper().strip().replace(' ', ''))[j]:
            if i != j:
                congruencias += 2
            else:
                congruencias += 1
        else:
            break
        j -= 1


print('\n', end='')
if congruencias == len(frase.replace(' ', '').strip()):
    print('\"{}\" É UM PALÍNDROMO.'.format(frase))
else:
    print('\"{}\" NÃO É UM PALÍNDROMO.'.format(frase))
'''

'''
# Algoritmo 2:
frase = str(input('Digite uma frase: ')).strip().replace(' ', '')

fraseInvertida = ''

for i in range(len(frase) - 1, -1, -1):
    fraseInvertida += frase[i]

print('\n\nA frase \"{}\" fica \"{}\" ao contrário. Portanto,'.format(frase.upper().replace(' ', ''),
                                                                      fraseInvertida.upper()
                                                                      ), end=' ')
if fraseInvertida.upper() != frase.upper().replace(' ', ''):
    print('NÃO', end=' ')
print('temos um PALÍNDROMO!')
'''

# Algoritmo 3 (sem for):
frase = str(input('Digite uma frase: ')).strip().replace(' ', '')

fraseInvertida = frase[::-1]  # Pega a string frase do início até o final, mas, com o salto -1, o programa começa a
# contar a partir do final

print('\n\nA frase \"{}\" fica \"{}\" ao contrário. Portanto,'.format(frase.upper().replace(' ', ''),
                                                                      fraseInvertida.upper()
                                                                      ), end=' ')
if fraseInvertida.upper() != frase.upper().replace(' ', ''):
    print('NÃO', end=' ')
print('TEMOS UM PALÍNDROMO!')
