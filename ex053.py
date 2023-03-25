frase = str(input('Digite uma frase: ')).strip("").replace(" ", "").lower()
print(frase)
if frase == frase[::-1]:
    print(f'A frase "{frase}" é um palíndromo')
else:
    print(f'A frase "{frase}" não é um palíndromo.')