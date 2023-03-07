num = int(input("Digite um número inteiro: "))
base_conversão = int(input("Digite '1' para binário, '2' para octal e '3' para hexadecimal: "))
if base_conversão == 1:
    convertido = bin(num)
    base = "binário"
elif base_conversão == 2:
    convertido = oct(num)
    base = "octal"
elif base_conversão == 3:
    convertido = hex(num)
    base = "hexadecimal"
else:
    print("Digite '1' para binário, '2' para octal e '3' para hexadecimal!")
print(f"O número inteiro {num} corresponde ao {base} {convertido[2:]}.")

'''
# Na resolução abaixo uso conceitos de looping while e for que ainda não foram trabalhados no Curso em Vídeo até a
# aula 12. Resolvi da maneira abaixo com o auxílio do ChatGPT. Mas não obtive esse código como está abaixo de uma só
# vez, em uma resposta. Fui perguntando como fazer as partes que eu queria fazer no código e fui juntando tudo em um código só.

num = int(input("Digite um número inteiro: "))
inteiro = num
base_conversão = int(input("Digite '1' para binário, '2' para octal ou '3' para hexadecimal: "))

if base_conversão == 1:
    divisor = 2
    restos = []

    while inteiro >= divisor:
        resto = inteiro % divisor
        restos.append(resto)
        inteiro = inteiro // divisor
    restos.append(inteiro)
    restos_invertido = list(reversed(restos))
    convertido = ''.join(str(i) for i in restos_invertido)
    #convertido = int(''.join(map(str, restos_invertido)))
    base = "binário"

elif base_conversão == 2:
    divisor = 8
    restos = []

    while inteiro >= divisor:
        resto = inteiro % divisor
        restos.append(resto)
        inteiro = inteiro // divisor
    restos.append(inteiro)
    restos_invertido = list(reversed(restos))
    convertido = ''.join(str(i) for i in restos_invertido)
    #convertido = int(''.join(map(str, restos_invertido)))
    base = "octal"

elif base_conversão == 3:
    divisor = 16
    restos = []

    while inteiro >= divisor:
        resto = inteiro % divisor
        restos.append(resto)
        inteiro = inteiro // divisor
    restos.append(inteiro)
    restos_invertido = list(reversed(restos))
    conversão_hexad_letras = {10: 'A', 11: 'B', 12: 'C', 13: 'D', 14: 'E', 15: 'F'}

    for i in range(len(restos_invertido)):
        if restos_invertido[i] in conversão_hexad_letras:
            restos_invertido[i] = conversão_hexad_letras[restos_invertido[i]]
    convertido = ''
    for item in restos_invertido:
        convertido += str(item)
    base = "hexadecimal"

else:
    print("Digite '1' para binário, '2' para octal ou '3' para hexadecimal!")
print(f"O número inteiro {num} corresponde ao {base} {convertido}.")

print(type(convertido))
'''