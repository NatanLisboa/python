# Mundo 3 - Aula 16 - Variáveis Compostas - Tuplas

# Exercício Python 076: Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços, na
# sequência. No final, mostre uma listagem de preços, organizando os dados em forma tabular.

produtos = ('Lápis', 1.75, 'Borracha', 2, 'Caderno', 15.9, 'Estojo', 25, 'Transferidor', 4.2,
            'Compasso', 9.99, 'Mochila', 120.32, 'Canetas', 22.3, 'Livro', 34.9)

print('\nExercício 76 – Lista de Preços com Tupla')
print('-' * 50)
print(f'{"TABELA DE PREÇOS":^60}')
print('-' * 50)
for posicao, produto in enumerate(produtos):
    if posicao % 2 == 0:
        print(f'{produto:.<40}', end='')
    else:
        print(f'R${produto:>7.2f}')
print('-' * 50)
