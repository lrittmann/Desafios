import time 
n1 = int(input('ESCOLHA UM NÚMERO: '))
n2 = int(input('ESCOLAH OUTRO NÚMERO: '))
opção = 0
maiornum = 0

while opção != 5:

    print('''
---MENU---
[1] Somar
[2] Multiplicar
[3] Maior
[4] Novos números
[5] Sair do programa
---MENU---
''')

    opção = int(input('ESCOLHA UMA OPÇÃO: '))

    if opção == 1:
        print(f'{n1} + {n2} = {n1+n2}')

    elif opção == 2:
        print(f'{n1} x {n2} = {n1*n2}')

    elif opção == 3:
        if n1 > n2:
            maiornum = n1           
        elif n2 > n1:
            maiornum = n2
        elif n1 == n2:
            print('Os números são iguais')
        else:
            print(f'O maior dos números é {maiornum}')

    elif opção == 4:
        n1 = int(input('ESCOLHA UM NÚMERO: '))
        n2 = int(input('ESCOLAH OUTRO NÚMERO: '))

    elif opção == 5:
        print('Encerrando programa..')

    else:
        print('Escolha entre 1 e 5')

time.sleep(1) 
print('Programa finalizado')  

