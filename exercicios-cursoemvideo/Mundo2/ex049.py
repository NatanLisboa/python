# Aula 13 - Estrutura de repetição for

# Desafio 049 - Refaça o DESAFIO 009, mostrando a tabuada de um número que o usuário escolher, só que agora utilizando
# um laço for.

print('\nDesafio 049 - Tabuada v2.0\n')
num = int(input('Digite um número inteiro para ver a sua tabuada: '))

print('\n', end='')
for i in range(0, 11):
    print('{} x {:2} = {:2}'.format(num, i, (num * i)))
