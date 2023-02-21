salário = float(input("Digite o seu salário: "))
if salário > 1250:
    novo_salário = salário + (salário * 0.1)
else:
    novo_salário = salário + (salário * 0.15)
print(f"Seu novo salário é R$ {novo_salário:.2f}")
