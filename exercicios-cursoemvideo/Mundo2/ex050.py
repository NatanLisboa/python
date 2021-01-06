# Aula 13 - Estrutura de repetição for

# Desafio 050 - Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem pares.
# Se o valor digitado for ímpar, desconsidere-o.

soma = 0
quantidadeDeNumerosPares = 0

print('\nDesafio 050 - Soma dos pares\n')
for i in range(1, 7):
    num = int(input('Digite o {}º número inteiro: '.format(i)))
    if num % 2 == 0:
        quantidadeDeNumerosPares += 1
        soma += num

print('\n', end='')
if quantidadeDeNumerosPares != 1:
    print('Soma dos {} números pares: {}'.format(quantidadeDeNumerosPares, soma))
else:
    print('Único número par digitado: {}'.format(soma))
