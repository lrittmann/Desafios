n = (int(input('Digite um número: ')), int(input('Digite um número: ')), int(input('Digite um número: ')), int(input('Digite um número: ')))
print(n)
cont = pos3 = 0
  
print(f'O número 9 apareceu {n.count(9)} vezes')

if 3 in n:
    print(f'O número 3 apareceu na {n.index(3)+1}ª posição')
else:
    print('O número 3 não foi digitado')

print('Os números pares encontrados foram = ', end = '')
for i in n:
    if i % 2 == 0:
        print(i, end = ' ')
