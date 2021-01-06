#  Desafio 013 bônus - Calcular os novos valores dos produtos considerando pagamentos à vista e parcelados
# Considere:
# Pagamento à vista -> 10% de desconto no valor total do produto
# Pagamento a prazo -> 8% de aumento no valor total do produto

print('Desafio 013 bônus - Pagamento à vista e a prazo')
valorProduto = float(input('Valor original do produto: R$'))
print('\nO produto passará a custar R${:.2f} se o valor original for pago à vista e R${:.2f}, caso o mesmo seja '
      'quitado a prazo.'.format(0.9 * valorProduto, 1.08 * valorProduto))
