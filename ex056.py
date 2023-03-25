média_idade = 0
maior_idade = 0
nome_homem = ''
pessoas = []
mulheres = 0

for c in range(0, 4):
    nome = str(input('Nome: '))
    idade = int(input('Idade: '))
    sexo = str(input('Sexo (m = masculino; f = feminino; nb = não-binário: '))
    pessoa = (nome, idade, sexo)
    pessoas.append(pessoa)
    nome, idade, sexo = pessoa
    média_idade += idade / 4
    if sexo == 'm' and idade > maior_idade:
        maior_idade = idade
        nome_homem = nome
    elif sexo == 'f' and idade < 20:
        mulheres += 1
print(f'A média de idade do grupo é {média_idade}')
print(f'O homem mais velho tem {maior_idade} anos e seu nome é {nome_homem} ')
print(f'{mulheres} mulher(es) te(ê)m menos de 20 anos de idade.')