# Desafio 004 - Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações
# possíveis sobre ele

coresLetra = {
    'padrao': '\033[m',
    'branco': '\033[30m',
    'vermelho': '\033[31m',
    'verde': '\033[32m',
    'amarelo': '\033[33m',
    'azul': '\033[34m',
    'lilas': '\033[35m',
    'verdeagua': '\033[36m',
    'cinza': '\033[37m',
    'negativo': '\033[7m'
}

print('{}Desafio 004{}'.format(coresLetra['negativo'], coresLetra['padrao']))
qualquerCoisa = str(input('Digite qualquer coisa: '))

print('\nTipo da coisa digitada: {}{}{}'.format(coresLetra['lilas'], type(qualquerCoisa), coresLetra['padrao']))

print('A string digitada somente contém espaços: ', end=''
                                                        '{}{}{}\n'.format(coresLetra['verdeagua'],
                                                                          qualquerCoisa.isspace(),
                                                                          coresLetra['padrao']))

print('A string digitada é um número: ', end=''
                                             '{}{}{}\n'.format(coresLetra['cinza'],
                                                               qualquerCoisa.isnumeric(),
                                                               coresLetra['padrao']))

print('A string digitada só contém letras: ', end=''
                                                  '{}{}{}\n'.format(coresLetra['amarelo'],
                                                                    qualquerCoisa.isalpha(),
                                                                    coresLetra['padrao']))

print('A string digitada contém somente letras ou números: ', end=''
                                                                  '{}{}{}\n'.format(coresLetra['verde'],
                                                                                    qualquerCoisa.isalnum(),
                                                                                    coresLetra['padrao']))

print('A string digitada está escrita somente com letras maiúsculas: ', end=''
                                                                            '{}{}{}\n'.format(coresLetra['vermelho'],
                                                                                              qualquerCoisa.isupper(),
                                                                                              coresLetra['padrao']))

print('A string digitada está escrita somente com letras minúsculas: ', end=''
                                                                            '{}{}{}\n'.format(coresLetra['branco'],
                                                                                              qualquerCoisa.islower(),
                                                                                              coresLetra['padrao']))

print('A string digitada está escrita em forma de título, ou seja, capitalizada (Ex.: Aaaaaaa): ', end=''
                                                                                                      '{}{}{}\n'.format(coresLetra['negativo'],
                                                                                                                        qualquerCoisa.istitle(),
                                                                                                                        coresLetra['padrao']))

print('A string digitada pode ser exibida na tela: {}'.format(qualquerCoisa.isprintable()))
