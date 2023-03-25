from datetime import date
maior = 0
menor = 0
for c in range(0, 7):
    birth = int(input('Digite o ano de nascimento no formato aaaa: '))
    idade = date.today().year - birth
    if idade >= 21:
        maior += c
    else:
        menor += c
print(f'{maior} pessoas são maiores de idade e {menor} pessoas são menores de idade.')
