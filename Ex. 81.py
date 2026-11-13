lista = []

while True:
    lista.append(int(input('Digite um número: ')))
    r = str(input('Quer continuar? [S/N]')).upper().strip()
    if r == 'N':
        break


print(f'A lista que você digitou tem: {len(lista)} elementos')
lista.sort(reverse=True)
print(f'A lista que você digitou em ordem decrescente é: {lista}')
if 5 in lista:
    print('O valor 5 faz parte da lista')
else:
    print('O valor 5 não faz parte da lista')
