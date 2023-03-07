import random
choices = ["Pedra", "Papel", "Tesoura"]
pc = random.choice(choices)
print(pc)
user = int(input("Pressione (1) para Pedra, (2) para Papel ou (3) para Tesoura: "))
print(f"O pc escolheu {pc} e você escolheu {user}!")
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
    print("Você deve pressionar (1) para Pedra, (2) para Papel ou (3) para Tesoura!")

print(f"{resultado} {ganhador}")


