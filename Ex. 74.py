import random
import sys
maiornum = 0
menornum = sys.maxsize

numeros = (random.randint(1,10), random.randint(1,10), random.randint(1,10), random.randint(1,10), random.randint(1,10), )

print(f'Os números são: {numeros}')

for i in numeros:
    if i > maiornum:
        maiornum = i

    elif i < menornum:
        menornum = i

print(f'O maior número é {maiornum}')
print(f'O menor número é {menornum}')