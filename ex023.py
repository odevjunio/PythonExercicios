'''num = int(input("Informe um número: "))
if num >= 0 and num < 10:
    print(f'Unidade: {num} \nDezena: 0 \nCentena: 0 \nMilhar: 0')
elif num >= 10 and num < 100:
    print(f'Unidade: {str(num)[-1]} \nDezena: {str(num)[-2]} \nCentena: 0 \nMilhar: 0')
elif num >= 100 and num < 1000:
    print(f'Unidade: {str(num)[-1]} \nDezena: {str(num)[-2]} \nCentena: {str(num)[-3]} \nMilhar: 0')
elif num >= 1000 and num < 10000:
    print(f'Unidade: {str(num)[-1]} \nDezena: {str(num)[-2]} \nCentena: {str(num)[-3]} \nMilhar: {str(num)[-4]}')
else:
    print("Informe um número válido!")'''

# Dessa maneira abaixo dá erro pois não contempla os casos de números com menos de 4 casas decimais

'''num = int(input("Informe um número: "))
n = str(num)
print(f'Analisando o número {num}:')
print(f'Unidade: {n[3]}')
print(f'Dezena: {n[2]}')
print(f'Centena: {n[1]}')
print(f'Milhar: {n[0]}')'''

'''num = int(input("Informe um número: "))
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10
print(u, d, c, m)'''

num = int(input("Informe um número: "))
print(f"Analisando o número {num}:")
print(f"Unidade: {num % 10}")
print(f"Dezena: {num // 10 % 10}")
print(f"Centena: {num // 100 % 10}")
print(f"Milhar: {num // 1000 % 10}")

































