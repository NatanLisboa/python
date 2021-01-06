# Aula 14 - Estrutura de repetição while (Estrutura de repetição com teste lógico)


# Exercício Python 70: Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar se o
# usuário vai continuar ou não. No final, mostre:

# A) qual é o total gasto na compra.

# B) quantos produtos custam mais de R$1000.

# C) qual é o nome do produto mais barato.

totalCompra = produtosQueCustamMais1000Reais = precoProdutoMaisBarato = 0
nomeProdutoMaisBarato = ''
codigoProduto = 0

print('\nDesafio 070 - Estatísticas em produtos\n')

while True:

    nomeProduto = str(input('Nome do produto: ')).strip()
    while True:
        precoProduto = str(input('Preço do produto: R$')).strip()
        if precoProduto.isnumeric() or \
                (precoProduto[:precoProduto.find('.')].isnumeric() and precoProduto[
                                                                       precoProduto.find('.') + 1:].isnumeric()
                 and len(precoProduto) == precoProduto.find('.') + 3):
            precoProduto = float(precoProduto)
            break
        else:
            print('\n\033[31mVALOR INVÁLIDO INSERIDO! POR FAVOR, DIGITE UM PREÇO VÁLIDO PARA O PRODUTO!\033[m\n')

    codigoProduto += 1

    totalCompra += precoProduto
    if precoProduto > 1000.0:
        produtosQueCustamMais1000Reais += 1
    if codigoProduto == 1 or precoProduto < precoProdutoMaisBarato:
        nomeProdutoMaisBarato = nomeProduto
        precoProdutoMaisBarato = precoProduto

    while True:
        continuarCompra = str(input('Deseja continuar colocando produtos no carrinho? [S/N]: ')).strip().upper()
        if continuarCompra == 'S' or continuarCompra == 'N':
            break
        else:
            print('\n\033[31mRESPOSTA INVÁLIDA! POR FAVOR, DIGITE "S" OU "N"\033[m\n')

    if continuarCompra == 'N':
        break

    print('\n', end='')

print(f'\n\nTotal a pagar: R${totalCompra:.2f}')
print(f'Quantidade de produtos que custam mais de R$1000,00: {produtosQueCustamMais1000Reais}')
print(f'Nome do produto mais barato: {nomeProdutoMaisBarato} (R${precoProdutoMaisBarato:.2f})')
