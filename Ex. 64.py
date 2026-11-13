n = 0
soma = 0
c = 0
while True:
    n = int(input('Digite um número: '))
    if n == 999:
        break
    soma += n   
    c += 1
    
print(f'Você falou o total de {c} números, que somam {soma}')