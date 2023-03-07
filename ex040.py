print("===== Calculadora de notas ======")
n1 = float(input("Nota na P1: "))
n2 = float(input("Nota na P2: "))
média = (n1 + n2) / 2

if média < 5.0:
    situação = "REPROVADO"
elif 5.0 <= média < 7:
    situação = "de RECUPERAÇÃO"
else:
    situação = "APROVADO"
print(f"Sua média é {média:.1f}. Você está {situação}!")