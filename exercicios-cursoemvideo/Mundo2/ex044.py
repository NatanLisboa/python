# Desafuio 044 - Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e
# condição de pagamento:

# - À vista dinheiro ou cheque: 10% de desconto
# - À vista no cartão: 5% de desconto
# - Em até 2x no cartão: Preço normal
# - 3x ou mais no cartão: 20% de juros

print('{:=^80}'.format(' Desafio 044 - Gerenciador de Pagamentos '))
precoProduto = float(input('Preço do produto: R$'))
condicaoPagamento = str(input('\n1 - À vista (dinheiro/cheque)'
                              '\n2 - À vista (cartão)'
                              '\n3 - Parcelado (cartão)\n\n'
                              'Selecione a forma de pagamento: '))

quantidadeParcelas = 1

print('\n', end='')
if not(condicaoPagamento.isnumeric()):
    print('\033[31mDigite uma das opções acima!\033[m')
    exit(1)
else:
    condicaoPagamento = int(condicaoPagamento)
    if condicaoPagamento == 1:
        precoProduto = 0.9 * precoProduto
    elif condicaoPagamento == 2:
        precoProduto = 0.95 * precoProduto
    elif condicaoPagamento == 3:
        quantidadeParcelas = str(input('Em quantas parcelas você deseja pagar: '))
        if (quantidadeParcelas.isnumeric()) and (int(quantidadeParcelas) > 1):
            quantidadeParcelas = int(quantidadeParcelas)
            if quantidadeParcelas >= 3:
                precoProduto = 1.2 * precoProduto
        else:
            print('\n\033[31mQuantidade inválida de parcelas inserida!\033[m')
            exit(2)
    else:
        print('\033[31mDigite uma das opções acima!\033[m')
        exit(1)

valorParcelas = precoProduto / quantidadeParcelas

print('\nO produto será quitado em {}x de R${:.2f}'.format(quantidadeParcelas, valorParcelas))
print('Total a pagar: R${:.2f}'.format(precoProduto))
