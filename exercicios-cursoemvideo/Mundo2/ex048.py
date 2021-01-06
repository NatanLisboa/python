# Aula 13 - Estrutura de repetição for

# Desafio 048 - Faça um programa que calcule a soma entre todos os números ímpares que são múltiplos de três e que se
# encontram no intervalo de 1 até 500.

soma = 0

print('\nDesafio 048 - Soma ímpares múltiplos de três\n')
for i in range(3, 501, 6):
    soma += i

print('A soma entre todos os {} números ímpares múltiplos de 3 presentes de 1 a 500 é: '.format(500 // 6),
      end='')
print('{}'.format(soma))
