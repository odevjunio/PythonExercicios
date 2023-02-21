import math
angulo = float(input('Digite o valor do ângulo: '))
angulo_rad = math.radians(angulo)
seno = math.sin(angulo_rad)
cosseno = math.cos(angulo_rad)
tangente = math.tan(angulo_rad)
print(f'O ângulo {angulo} tem o: \nseno igual a {seno:.2f} \no cosseno igual a {cosseno:.2f} \na tangente igual a'
      f' {tangente:.2f}')

# Acima, em import math eu poderia ter feito assim:

# from math import radians, sin, cos, tn. Mas eu teria que remover os math usados no resto do código. Ficaria assim:

from math import radians, sin, cos, tan
angulo = float(input("Digite o valor do ângulo: "))
angulo_rad = radians(angulo)
seno = sin(angulo_rad)
cosseno = cos(angulo_rad)
tangente = tan(angulo_rad)
print(f'O angulo de {angulo}º tem: \nSENO = {seno:.2} \nCOSSENO = {cosseno:.2} \nTANGENTE = {tangente:.2}')