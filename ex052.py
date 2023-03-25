n = int(input('Número: '))
restos = []
for c in range(1, n+1):
    resto = n % c
    restos.append(resto)
    if n <= 1:
        num = "não é primo!"
    elif 0 not in restos[1:-2] and restos[0] == 0 and restos[-1] == 0:
        num = "é primo!"
    else:
        num = "não é primo!"
print(f'{n} {num}')

numero = int(input("Digite um número inteiro: "))
if numero <= 1:
    print(f"{numero} não é primo.")
else:
    for i in range(2, numero // 2 + 1):
        if numero % i == 0:
            print(f"{numero} não é primo.")
            break
    else:
        print(f"{numero} é primo.")