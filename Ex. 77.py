palavras = ('teste', 'carro', 'suporte', 'aeiou')

for palavra in palavras:
    print(F'\nNa palavra {palavra} temos as vogais: ', end='')
    for letra in palavra:
        if letra in 'aeiou':
            print(letra, end= ' ')