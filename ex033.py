'''n1 = float(input("Digite um número: "))
n2 = float(input("Digite um número: "))
n3 = float(input("Digite um número: "))
numeros = [n1, n2, n3]
print(f"O maior número digitado é o {max(numeros)} e o menor número digitado é o {min(numeros)}.")'''

'''n1 = float(input("Digite um número: "))
n2 = float(input("Digite um número: "))
n3 = float(input("Digite um número: "))
if n1 > n2 and n1 > n3:
    maior = n1
elif n1 < n2 and n1 < n3:
    menor = n1
elif n2 > n1 and n2 > n3:
    maior = n2
elif n2 < n1 and n2 < n3:
    menor = n2
if n3 > n1 and n3 > n2:
    maior = n3
else:
    menor = n3
print(f"O maior número é o {maior} e o menor número é o {menor}")'''

a = int(input("Digite um número: "))
b = int(input("Digite um número: "))
c = int(input("Digite um número: "))
menor = a
if b < a and b < c:
    menor = b
if c < a and c < b:
    menor = c
maior = a
if b > a and b > c:
    maior = b
if c > a and c > b:
    maior = c
print(f"O menor valor digitado foi {menor}")
print(f"O maior valor digitado foi {maior}")