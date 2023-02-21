distância = float(input("Qual a distância da viagem? "))
if distância <= 200:
    preço = distância * 0.5
else:
    preço = distância * 0.45
print(f"O preço da sua passagem será de R${preço:.2f}.")