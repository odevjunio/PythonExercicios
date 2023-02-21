medida = float(input('Digite a medida em metros: '))
print(f'A medida digitada foi {medida}m, que equivale a: \n{(medida / 1000):.3f}km \n{(medida / 100):.2f}hm \n{(medida / 10):.1f}dam \n{(medida * 10):.0f}dm \n{(medida * 100):.0f}cm \n{medida * 1000:.0f}mm')
