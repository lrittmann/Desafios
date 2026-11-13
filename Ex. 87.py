matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
pares = somacoluna = maior = 0
for linha in range(0, 3):
    for coluna in range(0, 3):
        matriz[linha][coluna] = int(input(f'Digite um valor para a posição [{linha}], [{coluna}] '))
        
        if matriz[linha][coluna] % 2 == 0:
            pares += matriz[linha][coluna]
        
        if coluna == 2:
            somacoluna += matriz[linha][coluna]

        if linha == 1:
            if matriz[linha][coluna] > maior:
                maior = matriz[linha][coluna]
                
for linha in range(0, 3):
    for coluna in range(0, 3):
        print(f'[{matriz[linha][coluna]}]', end='')
    print()

print('-=' * 40)
print(f'A soma dos valores pares é: {pares}')
print(f'A soma dos valores da terceira coluna é: {somacoluna}')
print(f'O maior valor da segunda linha é: {maior}')
print('-=' * 40)