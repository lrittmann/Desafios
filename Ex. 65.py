import sys
cont = maiornum = soma = 0
menornum = sys.maxsize
while True:
    numeros = int(input('Digite um número: '))
    pergunta = input('Deseja continuar: ').lower().strip()
    cont += 1
    soma += numeros

    if numeros > maiornum:
        maiornum = numeros
    elif numeros < menornum:
        menornum = numeros

    media = soma/cont

    if pergunta == 'não':
        break
print(f'~~~~~~~~~~\n\nO maior número é {maiornum}\nO menor número é {menornum}\nE a média é {media}\n\n~~~~~~~~~~')