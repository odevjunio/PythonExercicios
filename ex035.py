r1 = float(input("Digite o valor da primeira reta (r1): "))
r2 = float(input("Digite o valor da segunda reta (r2): "))
r3 = float(input("Digite o valor da terceira reta (r3): "))
'''if r1 < (r2 + r3) and r1 > ((-1)*(r2 - r3)):
    print(f"r1: {r1} \nr2: {r2} \nr3: {r3} \nUm triângulo pode ser construído com essas retas.")
elif r2 < (r1 + r3) and r2 > ((-1) * (r1 - r3)):
    print(f"r1: {r1} \nr2: {r2} \nr3: {r3} \nUm triângulo pode ser construído com essas retas.")
elif r3 < (r1 + r2) and r3 > ((-1) * (r1 - r2)):
    print(f"r1: {r1} \nr2: {r2} \nr3: {r3} \nUm triângulo pode ser construído com essas retas.")
else:
    print(f"r1: {r1} \nr2: {r2} \nr3: {r3} \nNão é possível construir um triângulo com essas retas.")'''
if r1 < r2 + r3 and r2 < r1 + r3 and r3 <r1 + r2:
    print("Os segmentos acima podem formar um triângulo!")
else:
    print("Os segmentos acima não podem formar um triângulo.")