tabela = ('Palmeiras', 'Flamengo', 'Athletico-PR', 'Fluminense', 'Cruzeiro', 'Bahia', 'Corinthians', 'Bragantino', 'Botafogo', 'Coritiba', 'Atlético-MG', 'São Paulo',
          'Vitória', 'Grêmio', 'Mirassol', 'Internacional', 'Santos', 'Vasco', 'Remo', 'Chapecoense')

print('----TABELA BRASILEIRÃO----')
print(f'[A] Os cinco primeiros colocados são: {tabela[0:5]}')
print(f'[B] Os últimos colocados são: {tabela[16:20]}')
print(f'[C] Lista com os times em ordem alfabética: {sorted(tabela)}')
print(f'[D] A chapecoense está na posição: {tabela.index('Chapecoense')+1}')