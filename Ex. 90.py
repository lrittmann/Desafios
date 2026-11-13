aluno = {'nome': input('Nome: '), 'media': float(input(f'Media do aluno: '))}

print(f' - nome é igual a {aluno['nome']}')
print(f' - média é igual a {aluno['media']}')

if aluno['media'] < 7:
    print(f' - situação é igual a Recuperação')
elif aluno['media'] < 5:
    print(f' - situação é igual a Reprovado')
elif aluno['media'] >= 7:
    print(f' - situação é igual a Aprovado')