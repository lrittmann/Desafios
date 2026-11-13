import sys
pessoa = []
grupo = []
maispesado = []
menospesado = []
maiorpeso = 0
menorpeso = sys.maxsize

while True:
    pessoa.append(input('Nome: '))
    pessoa.append(int(input('Peso: ')))
    
    if pessoa[1] > maiorpeso:
        maiorpeso = pessoa[1]
    if pessoa[1] < menorpeso:
        menorpeso = pessoa[1]
        
    grupo.append(pessoa[:])
    pessoa.clear()
    r = input('Quer continuar? [S/N]').strip().upper()

    while r not in 'SN':
        print('Opção inválida, tente novamente...')
        r = input('Quer continuar? [S/N]').strip().upper()
    if r == 'N':
        break
'''
for p in grupo:
    if p[1] > maiorpeso:
        maiorpeso = p[1]
        maispesado.clear()
        maispesado.append(p[0])
    
    elif p[1] == maiorpeso:
        maispesado.append(p[0])

    if p[1] < menorpeso:
        menorpeso = p[1]
        menospesado.clear()
        menospesado.append(p[0])  

    elif p[1] == menorpeso:
        menospesado.append(p[0])  
'''
for p in grupo:
    if p[1] == maiorpeso:
        print(f'p[0]')



print(f'Ao todo você cadastrou {len(grupo)} pessoas')
print(f'O maior peso foi de {maiorpeso} Kg. Peso de: {maispesado}')
print(f'O menor peso foi de {menorpeso} Kg. Peso de: {menospesado}')


