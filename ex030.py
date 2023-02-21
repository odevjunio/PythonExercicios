'''num = str(input("Digite um número inteiro: "))
if num[-1] in [str(i) for i in list(range(0, 10, 2))]:
    print(f"{num} é par")
else:
    print(f"{num} é ímpar")'''

número = int(input("Me diga um número qualquer: "))
resultado = número % 2
if resultado == 0:
    print(f"O número {número} é par!")
else:
    print(f"O número {número} é impar.")