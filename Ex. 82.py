listainteira = [] 
listapar = []
listaimpar = []

while True:
    n = int(input('Digite um número:'))
    r = str(input('Quer continuar? [S/N] ')).strip().upper()
    listainteira.append(n)
    
    if n % 2 == 0:
        listapar.append(n)
    else:
        listaimpar.append(n)
    if r == 'N':
        break

print(f'Lista inteira: {listainteira}')
print(f'Lista de pares: {listapar}')
print(f'Lista de impares: {listaimpar}')