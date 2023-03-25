peso = float(input("Peso: "))
altura = float(input("Altura: "))
imc = peso / altura ** 2

if imc < 18.5:
    condição = "Cuidado! Você está abaixo do peso."
elif imc < 25:
    condição = "Ótimo! Você está com peso ideal."
elif imc < 30:
    condição = "Você está com sobrepeso."
elif imc < 40:
    condição = "Cuidado! Você está em um quadro de obesidade."
else:
    condição = "ATENÇÃO! Você está em um quadro de obesidade mórbida. Procure um médico."

print(f"Seu IMC está igual a {imc:.1f}. {condição}")