# Mundo 3 - Aula 16 - Variáveis Compostas - Tuplas

# Exercício Python 077: Crie um programa que tenha uma tupla com várias palavras (não usar acentos). Depois disso, você
# deve mostrar, para cada palavra, quais são as suas vogais

palavras = ('APRENDER', 'PROGRAMAR', 'LINGUAGEM', 'PYTHON', 'CURSO', 'GRATIS', 'ESTUDAR', 'PRATICAR', 'TRABALHAR',
            'MERCADO', 'PROGRAMADOR', 'FUTURO')

print('\nExercício 77 – Contando vogais em Tupla\n')
for palavra in palavras:
    print(f'Na palavra {palavra} temos ', end='')
    for letra in palavra:
        if letra.upper() in 'AEIOU':
            print(letra, end=' ')
    print('\n', end='')
