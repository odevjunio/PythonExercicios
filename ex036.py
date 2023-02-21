valor = float(input("Qual é o valor da casa? "))
salário = float(input("Qual é o valor do seu salário? "))
anos = int(input("Em quantos anos quer parcelar a casa? "))
prestação = (valor / (anos * 12))
if prestação >= (salário * 0.3):
    print("Você não pode fazer esse empréstimo pois a prestação do mesmo é maior ou igual a 30% do seu salário.")
else:
    print(f"O valor do seu empréstimo é R${valor:.2f} e cada prestação do mesmo é R${prestação:.2f}. \nSeu empréstimo "
          f"será quitado em {anos} anos, e o valor da prestação é menor que 30% do seu salário ("
          f"{prestação / salário * 100:.2f})%")