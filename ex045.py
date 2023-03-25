'''import random
choices = ["Pedra", "Papel", "Tesoura"]
pc = random.choice(choices)
print(pc)
user = int(input("Pressione (1) para Pedra, (2) para Papel ou (3) para Tesoura: "))
if user == 1:
    user_choice = "Pedra"
elif user == 2:
    user_choice = "Papel"
elif user == 3:
    user_choice = "Tesoura"
print(f"O pc escolheu {pc} e você escolheu {user_choice}!")
pedra_papel = "O papel embrulha a pedra."
pedra_tesoura = "A pedra quebra a tesoura."
tesoura_papel = "A tesoura corta o papel."
pc_vence = "O pc te venceu!"
user_vence = "Parabéns, você ganhou do pc!"

if pc == "Pedra" and user == 2:
    resultado = pedra_papel
    ganhador = user_vence
elif pc == "Papel" and user == 3:
    resultado = tesoura_papel
    ganhador = user_vence
elif pc == "Tesoura" and user == 1:
    resultado = pedra_tesoura
    ganhador = user_vence
elif pc == "Papel" and user == 1:
    resultado = pedra_papel
    ganhador = pc_vence
elif pc == "Tesoura" and user == 2:
    resultado = tesoura_papel
    ganhador = pc_vence
elif pc == "Pedra" and user == 3:
    resultado = pedra_tesoura
    ganhador = pc_vence
else:
    resultado = "Você e o pc escolheram a mesma opção,"
    ganhador = "então não há um ganhador!"

print(f"{resultado} {ganhador}")
'''

'''import random, time
choices = ["Pedra", "Papel", "Tesoura"]
pc = random.choice(choices)
print(pc)
user = int(input("Suas opções: \n[ 0 ] PEDRA\n[ 1 ] PAPEL \n[ 2 ] TESOURA\nQual é a sua jogada? "))
if user == 0:
    user_choice = "Pedra"
elif user == 1:
    user_choice = "Papel"
elif user == 2:
    user_choice = "Tesoura"
time.sleep(0.5)
print("JO")
time.sleep(0.5)
print("KEN")
time.sleep(0.5)
print("PO!!!")
time.sleep(0.5)
print(f"-=-=-=-=-=-=-=-=-=-=\nComputador jogou {pc}\nJogador jogou {user_choice}\n-=-=-=-=-=-=-=-=-=-=")
pc_vence = "COMPUTADOR VENCE"
user_vence = "JOGADOR VENCE"

if pc == "Pedra" and user == 1:
    ganhador = user_vence
elif pc == "Papel" and user == 2:
    ganhador = user_vence
elif pc == "Tesoura" and user == 0:
    ganhador = user_vence
elif pc == "Papel" and user == 0:
    ganhador = pc_vence
elif pc == "Tesoura" and user == 1:
    ganhador = pc_vence
elif pc == "Pedra" and user == 2:
    ganhador = pc_vence
else:
    ganhador = "EMPATE"
print(f"{ganhador}")'''

from random import randint
from time import sleep
itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0, 2)
print('''Suas opções:
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA''')
jogador = int(input('Qual é a sua jogada? '))
sleep(0.5)
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO!!!')
sleep(1)
print('-='*10)
print(f'Computador jogou {itens[computador]}')
print(f'Jogador jogou {itens[jogador]}')
print('-='*10)
if computador == 0:
    if jogador == 0:
        print('EMPATE')
    elif jogador == 1:
        print('JOGADOR VENCE')
    elif jogador == 2:
        print('COMPUTADOR VENCE')
    else:
        print('JOGADA INVÁLIDA!')

elif computador == 1:
    if jogador == 0:
        print('COMPUTADOR VENCE')
    elif jogador == 1:
        print('EMPATE')
    elif jogador == 2:
        print('JOGADOR VENCE')
    else:
        print('JOGADA INVÁLIDA!')
elif computador == 2:
    if jogador == 0:
        print('JOGADOR VENCE')
    elif jogador == 1:
        print('COMPUTADOR VENCE')
    elif jogador == 2:
        print('EMPATE')
    else:
        print('JOGADA INVÁLIDA!')
