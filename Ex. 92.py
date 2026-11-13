nome = input('Nome: ')
ano = int(input('Ano de Nascimento: '))
carteira = int(input('Carteira de trabalho (0 se não tiver): '))
informações = {'nome': nome, 'ano': 2026-ano, 'carteira': carteira}

if carteira != 0:
    ano_contratação = int(input('Ano de contratação: '))
    informações['contratação'] = ano_contratação
    salario = int(input('Salário: '))
    informações['salário: R$'] = salario
    if ano_contratação - 2026 < 35:
        informações['aposentadoria'] = 'Não vai aposentar'
    else:
        informações['aposentadoria'] = 100
    print('-=' *35)
    for k, v in informações.items():
        print(f'  - {k} tem o valor {v}')

if carteira == 0:
    for k, v in informações.items():
        print(f'  - {k} tem o valor {v}')