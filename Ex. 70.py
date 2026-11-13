import sys
nomebarato = ''
maisbarato = sys.float_info.max
valortotal = contpreço = 0
while True:
    nome = str(input('Nome do produto: '))
    preço = float(input('Preço do produto: '))
    valortotal += preço

    if preço > 1000:
        contpreço += 1
    
    if preço < maisbarato:
        maisbarato = preço
        nomebarato = nome

    continuar = ' '
    while continuar not in 'SsNn':
        continuar = str(input('Deseja continuar? [S/N] ')).upper().strip()
    if continuar == 'N':
        break
print(f'O total gasto em produtos foi R${valortotal}')
print(f'{contpreço} produtos custaram mais que R$1.000,00')
print(f'O produto mais barato foi o(a) {nomebarato}, custando R${maisbarato}')

