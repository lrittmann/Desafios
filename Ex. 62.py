n = int(input('Primeiro termo: '))
r = int(input('Razão da P.A.: '))
x = n
termos = 10
contador = 0
while termos != 0:
    for i in range(termos):
        contador += 1
        print(f'{x} -> ', end='')
        x += r
    print('PAUSA')
    termos = int(input('\nquantos mais termos você quer? '))
print('Fim')
print(f'Você visualizou {contador} termos')