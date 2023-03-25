pessoas = [('João', 30, 'M'), ('Maria', 25, 'F'), ('Pedro', 35, 'M'), ('Lucas', 28, 'M')]

maior_idade = 0
nome_pessoa = ''

for pessoa in pessoas:
    nome, idade, sexo = pessoa
    if sexo == 'M' and idade > maior_idade:
        maior_idade = idade
        nome_pessoa = nome

print(f"A pessoa do sexo masculino com a maior idade é {nome_pessoa}, com {maior_idade} anos.")