listanum = []
while True:
    teclado = int(input('Digite um número: '))
    
    if teclado not in listanum:
        listanum.append(teclado)
    else:
        print('Número já inserido na lista, tente outro')

    pergunta = input('Você deseja continuar? [S/N] ').upper().strip()

    if pergunta == 'N':
            break

listanum.sort()
print(f'Você digitou os valores {listanum}')