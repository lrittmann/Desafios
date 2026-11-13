listanumeros = []

for i in range(0, 5):
    n = int(input('Digite um número: '))
    if i == 0:
        listanumeros.append(n)

    elif n > listanumeros[-1]:
        listanumeros.append(n)

    else:
        pos = 0
        while pos < len(listanumeros):
            if n <= listanumeros[pos]:
                listanumeros.insert(pos, n)
                break
            pos += 1

print(f'Os valores digitados em ordem foram {listanumeros}')