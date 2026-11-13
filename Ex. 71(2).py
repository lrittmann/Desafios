valor = int(input("Digite o valor que deseja retirar: "))
total = valor
cédula = 50
contador50 = 0
while True:
    if cédula >= total:
        total -= cédula
        contador50 += 1
        break

print(total, contador50)

