n = int(input('Digite um número para saber sua tabuada de multiplicação: '))
print('-'*12)
for c in range(1, 11):
    tabuada = c * n
    print(f'{n} x {c} = {tabuada}')
print('-'*12)