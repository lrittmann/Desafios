e = input('Digite uma expressão: ')
contador = 0

for i in e:
    
    if i == '(':
        contador += 1
    if i == ')':
        contador -= 1
    if contador < 0:
        break
    

if contador == 0:
    print('Expressão válida!')

elif contador < 0 or contador > 0:
    print('Expressão inválida!')