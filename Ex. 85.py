numeros = []
pares = []
impares = []
for i in range(0, 7):
    numeros.append(int(input('Digite um número: ')))
    if numeros[i] % 2 == 0:
        pares.append(numeros[i])
    else:
        impares.append(numeros[i])

pares.sort()
impares.sort()
print(f'Todos os números: {numeros}')
print(f'Todos os pares: {pares}')
print(f'Todos os ímpares: {impares}')