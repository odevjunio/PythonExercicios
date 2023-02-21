from random import randint
from time import sleep
num_sorteado = randint(0, 5)
num_usuario = int(input("Descubra qual número foi sorteado entre 0 e 5: "))
print("Sorteando...")
sleep(3)
if num_usuario == num_sorteado:
    print("Parabéns, você acertou o número que eu sorteei!")
else:
    print(f"Você errou! Eu sorteei o número {num_sorteado} e você chutou o número {num_usuario} Tente novamente!")