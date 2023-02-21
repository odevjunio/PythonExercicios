'''frase = input("Digite uma frase: ")
print(f"A letra 'A' aparece {frase.upper().count('A')} vezes na frase digitada.")
print(f"A letra 'A' aparece pela primeira vez na posição {frase.upper().find('A')}, e pela última vez na posição "
      f"{frase.upper().rfind('A')}")'''

frase = str(input("Digite uma frase: ")).upper().strip()
print(f"A letra A aparece {frase.count('A')} vezes na frase.")
print(f"A primeira letra A apareceu na posição {frase.find('A')+1}")
print(f"A última letra A apareceu na posição {frase.rfind('A')+1}")