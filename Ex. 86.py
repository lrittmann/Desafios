n = [[], [], []]
for i in range(0, 9):
    if i < 3:
        n[0].append(int(input('Digite um numero: ')))
        i += 1
    elif i < 6:
        n[1].append(int(input('Digite um numero: ')))
        i += 1
    elif i < 9:
        n[2].append(int(input('Digite um numero: ')))
        i += 1
    
    


print(n[0])
print(n[1])
print(n[2])