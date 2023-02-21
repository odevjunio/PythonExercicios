velocidade = float(input("Velocidade do veículo: "))
if velocidade > 80:
    print(f"Você está dirigindo a {velocidade:.1f} km/h e por esse motivo foi multado em R"
          f"${((velocidade - 80) * 7):.2f}, pois o limite de "
          f"velocidade permitido "
          f"nessa via, que é de 80km/h.")
print(f"Sua velocidade é de {velocidade:.1f} km/h. Tenha um bom dia e continue a dirigir com segurança!")