import math
cateto_a = float(input('Digite o valor do cateto oposto: '))
cateto_b = float(input('Digite o valor do cateto adjacente: '))
hipotenusa = math.hypot(cateto_a, cateto_b)
print(hipotenusa)

cateto_a = float(input("Digite o valor do cateto oposto: "))
cateto_b = float(input("Digite o valor do cateto adjacente: "))
hipotenusa = ((cateto_a**2) + (cateto_b**2))**(1/2)
print(hipotenusa)