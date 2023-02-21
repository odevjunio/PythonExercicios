import math
num = float(input('Digite um valor: '))
inteiro = math.floor(num)
print(f'O número {num} tem a porção inteira é {inteiro}.')

from math import trunc  # essa forma, usando o from, tbm pode ser usada
num = float(input("Digite um número: "))
inteiro = trunc(num)
print(f'O número digitado é {num} e sua parte inteira é {inteiro}.')

num = float(input("Digite um número: "))
inteiro = int(num)
print(f'O número digitado é {num} e sua parte inteira é {inteiro}.')


