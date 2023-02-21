preço = float(input('Digite o preço do produto: R$'))
desconto = 0.05
preço_final = preço - (preço * desconto)
print(f'R${preço_final:5.2f}')
