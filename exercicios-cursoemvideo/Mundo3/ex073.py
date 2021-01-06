# Mundo 3 - Aula 16 - Variáveis Compostas - Tuplas

# Exercício Python 73: Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro de
# Futebol, na ordem de colocação. Depois mostre:
#
# a) Os 5 primeiros times.
#
# b) Os últimos 4 colocados.
#
# c) Times em ordem alfabética.
#
# d) Em que posição está o time da Chapecoense.

timesBrasileirao2018 = ('Corinthians', 'Palmeiras', 'Santos', 'Grêmio', 'Cruzeiro', 'Flamengo', 'Vasco', 'Chapecoense',
                        'Atlético', 'Botafogo', 'Atlético-PR', 'Bahia', 'São Paulo', 'Fluminense', 'Sport Recife',
                        'EC Vitória', 'Coritiba', 'Avaí', 'Ponte Preta', 'Atlético-GO')

print('\nExercício 73 – Tuplas com Times de Futebol\n')
print(f'Tabela de times do Brasileirão:\n\n{timesBrasileirao2018}')
print(f'\n\n5 primeiros colocados do Brasileirão:\n\n{timesBrasileirao2018[0:5]}')
print(f'\n\n4 últimos colocados do Brasileirão:\n\n{timesBrasileirao2018[-4:]}')
print(f'\n\nTimes em ordem alfabética: {sorted(timesBrasileirao2018)}')
print(f'\n\nPosição da Chapecoense: {timesBrasileirao2018.index("Chapecoense") + 1}º')