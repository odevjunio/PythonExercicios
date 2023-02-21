'''nome = input("Digite seu nome completo: ")
print(f'Primeiro nome: {nome.split()[0]}')
print(f'Último nome: {nome.split()[-1]}')'''

nome = str(input("Digite seu nome completo: ")).strip().split()
print("Muito prazer em te conhecer!")
print(f"Seu primeiro nome é {nome[0]}")
print(f"Seu último nome é {nome[-1]}")






