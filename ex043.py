peso = float(input("Peso: "))
altura = float(input("Altura: "))
imc = peso / altura ** 2

if imc < 18.5:
    condição = "abaixo do peso"
elif imc < 25:
    condição = "com peso ideal"
elif imc < 30:
    condição = "com sobrepeso"
elif imc < 40:
    condição = "em um quadro de obesidade"
else:
    condição = "em um quadro de obesidade mórbida"

print(f"Você está {condição}.")