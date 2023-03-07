lado1 = float(input("Digite o valor de um dos lados do triângulo: "))
lado2 = float(input("Digite o valor de mais um dos lados do triângulo: "))
lado3 = float(input("Digite o valor do último lado do triângulo: "))

if ((lado2 + lado3) > lado1) and ((lado1 + lado2) > lado3) and ((lado1 + lado3) > lado2):

    if lado1 != lado2 and lado2 != lado3 and lado1 != lado3:
        tipo = "ESCALENO"
    elif ((lado1 != lado2 and lado3) and lado2 == lado3) or ((lado2 != lado1 and lado3) and lado1 == lado3) or ((lado3 != lado1 and lado2) and lado1 == lado2):
        tipo = "ISÓSCELES"
    else:
        tipo = "EQUILÁTERO"

    print(f"O triângulo com lados iguais a {lado1}, {lado2} e {lado3} pode ser construído e será do tipo {tipo}.")

else:
    print(f"O triângulo com lados iguais a {lado1}, {lado2} e {lado3} não pode ser construído.")