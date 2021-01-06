#  Desafio 006 - Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada.

coresFundo = {
    'padrao': '\033[m',
    'branco': '\033[40m',
    'vermelho': '\033[41m',
    'verde': '\033[42m',
    'amarelo': '\033[43m',
    'azul': '\033[44m',
    'lilas': '\033[45m',
    'verdeagua': '\033[46m',
    'cinza': '\033[47m'
}

print('Desafio 006 - Dobro, triplo e raiz quadrada de um número')
n = int(input('Digite um número: '))
print('O dobro de {}{}{} é {}{}{}'.format(coresFundo['verdeagua'],
                                          n,
                                          coresFundo['padrao'],
                                          coresFundo['cinza'],
                                          n * 2,
                                          coresFundo['padrao']))

print('{}O{} {}triplo{} {}de{} {}{}{} {}é{} {}{}{}'.format(coresFundo['padrao'],
                                                           coresFundo['branco'],
                                                           coresFundo['vermelho'],
                                                           coresFundo['verde'],
                                                           coresFundo['amarelo'],
                                                           coresFundo['azul'],
                                                           coresFundo['lilas'],
                                                           n,
                                                           coresFundo['verdeagua'],
                                                           coresFundo['cinza'],
                                                           '\033[7m',
                                                           '\033[4;34m',
                                                           n * 3,
                                                           coresFundo['padrao']))

print('A raiz quadrada de {} é {}'.format(n, pow(n, (1/2))))
