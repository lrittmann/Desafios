from random import randint
from operator import itemgetter
maiorvalor = 0
jogadores = {'Jogador1': randint(1, 10), 'Jogador2': randint(1,10), 'Jogador3': randint(1,10), 'Jogador4': randint(1,10)}
rank = {}

for k, v in jogadores.items():
    print(f'O jogador {k}, tirou: {v}')

rank = sorted(jogadores.items(), key=itemgetter(1), reverse=True)
print(rank)