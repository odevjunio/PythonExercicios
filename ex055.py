pesos = []
for c in range(0, 4):
    peso = float(input('Digite seu peso: '))
    pesos.append(peso)
print(f'Maior peso: {max(pesos)} \n'
      f'Menor peso: {min(pesos)}')