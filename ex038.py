num_1 = int(input("Digite um número inteiro: "))
num_2 = int(input("Digite mais um número inteiro: "))

if num_1 > num_2:
    inteiro = num_1
    condição = "primeiro valor"
elif num_2 > num_1:
    inteiro = num_2
    condição = "segundo valor"
else:
    print("Não existe valor maior, os dois são iguais.")
    exit()
print(f"O {condição} ({inteiro}) é maior.")