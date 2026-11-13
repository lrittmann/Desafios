n = int(input('Primeiro termo: '))
r = int(input('Razão da P.A.: '))
x = n 
count = 0
while count < 10:
    count += 1
    print(x, ' ', end='')
    x += r
print('FIM!')

