lista = ('lapis', 5.4, 'leite', 3.50, 'frango', 10.90)

print('-' *20)
print('LISTAGEM DE PREÇOS')
print('-' *20)

for pos in range(0, len(lista)):
    if pos % 2 == 0:
        print(lista[pos],'....', end ='')
    else:
        print(f'R${lista[pos]}')
    
    