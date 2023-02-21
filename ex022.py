nome = str(input("Digite seu nome completo: ")).strip()   # esse .strip() remove espaços em branco antes e depois da
# string
print(f'Maiúsculas: {nome.upper()}')
print(f'Minúsculas: {nome.lower()}')
print(f"Número de ítens na string (descontando os espaços em branco): {(len(nome)) - (nome.count(' '))}")
print(f"Número de ítens na string (contando com os espaços em branco): {len(nome)}")
dividido = nome.split()
print(f"Número de letras no primeiro nome: {len(dividido[0])}")
print(f"Número de letras no primeiro nome: {nome.find(' ')}")
