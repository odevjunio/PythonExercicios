dias = int(input('Quantos dias alugados? '))
km = float(input('Quantos km rodados? '))
valor_dia = 60
valor_km = 0.15
print(f'O total a pagar é de R${((dias * valor_dia) + (km * valor_km)):.2f}.')