from random import randint
from time import sleep
p = [int(input('Quantos jogos você quer sortear? '))] 
lista = []
cont = 0


print('-'*43)
print('------------ JOGO DA MEGA SENA ------------')
print('-'*43)



print(f'SORTEANDO {p[0]} JOGOS')    
for jogos in range(p[0]):
    cont += 1
    p.clear()
    for numeros in range(0, 6):
        num = randint(1, 60)
        if num not in p:
            p.append(num)
        else:
            p.append('REPETIDO')   

    print(f'Jogo {cont}: {p}')
    sleep(1)
