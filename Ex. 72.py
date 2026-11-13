
base = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove',
        'dez', 'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito',
        'dezenove', 'vinte')

while True:

    n = int(input('Digite um número de 0 a 20: '))

    if n >= 0 and n <= 20:
        print(f'O número que você digitou foi {base[n]}')
        break

    else:  
        n = int(input('INVÁLIDO.. Digite um número de 0 a 20: '))