algo = input('Digite algo: ')
def is_capitalized(algo):
    return algo.isalpha() and algo[0].isupper() and algo[1:].islower()
print(f'O tipo primitivo desse valor é {type(algo)}.')
print(f'Só tem espaços? {algo.isspace()}')
print(f'É um número? {algo.isnumeric()}')
print(f'É alfabético? {algo.isalpha()}')
print(f'É alfanumérico? {algo.isalnum()}')
print(f'Está em maiúsculas? {algo.isupper()}')
print(f'Está em minúsculas? {algo.islower()}')
print(f'Está capitalizada? {is_capitalized(algo)}')
print(f'Está capitalizada? {algo.istitle()}')
