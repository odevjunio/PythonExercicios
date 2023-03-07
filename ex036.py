valor = float(input("Qual é o valor da casa? R$ "))
salário = float(input("Qual é o valor do seu salário? R$ "))
anos = int(input("Em quantos anos quer parcelar a casa? "))
prestação = valor / (anos * 12)
mínimo = salário * 0.3
if prestação >= (mínimo):
    print(f"EMPRÉSTIMO NEGADO! Motivo: A prestação do empréstimo (R$ {prestação:.2f}) é maior ou igual a 30% "
          f"do seu "
          f"salário.")
else:
    print(f"EMPRÉSTIMO APROVADO! \nValor do empréstimo: R${valor:.2f} \nValor da prestação é menor que 30% do seu "
          f"salário ("
          f"{prestação / salário * 100:.2f}%). \nPrestação: R"
          f"${prestação:.2f} \nSeu "
          f"empréstimo "
          f"será quitado em {anos} anos.")