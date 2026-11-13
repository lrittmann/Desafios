cadastro = []

while True:
    nome = input('Nome: ')
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))
    media = (nota1 + nota2) / 2

    cadastro.append([nome, [nota1, nota2], media])
    resposta = input('Você quer continuar? [S/N] ').upper()

    
    if resposta in 'Nn': 
        break

for i, a in enumerate (cadastro):
    print(f'Código. {i}  Nome: {a[0]}  Notas: {a[1]}  Média: {2}')


