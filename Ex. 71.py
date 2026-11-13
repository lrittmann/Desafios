cedulas50 = 0
cedulas20 = 0
cedulas10 = 0
cedulas1 = 0
while True:
    preço = int(input('Informe o valor a ser sacado: '))
    valor = preço
    if valor >= 50:
        cedulas50 = valor // 50
        valor -= cedulas50 * 50
        cedulas20 = valor // 20
        valor -= cedulas20 * 20
        cedulas10 = valor // 10
        valor -= cedulas10 * 10
        cedulas1 = valor // 1
        valor -= cedulas1 * 1
        break
    if valor >= 20:
        cedulas20 = valor // 20
        valor -= cedulas20 * 20
        cedulas10 = valor // 10
        valor -= cedulas10 * 10
        cedulas1 = valor // 1
        valor -= cedulas1 * 1
        break
    if valor >= 10:
            cedulas10 = valor // 10
            valor -= cedulas10 *10
            cedulas1 = valor // 1
            valor -= cedulas1 * 1
            break
    if valor >= 1:
                cedulas1 = valor // 1
                valor -= cedulas1 * 1
                break   

print(f'Cédulas de R$50 = {cedulas50}')
print(f'Cédulas de R$20 = {cedulas20}')
print(f'Cédulas de R$10 = {cedulas10}')
print(f'Cédulas de R$1 = {cedulas1}')