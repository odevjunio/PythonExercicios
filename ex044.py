preço = float(input("Preço do produto: R$ "))
pagamento = int(input("Escolha a forma de pagamento (pressione o número que corresponde à forma de pagamento): \n1 - "
                      "À vista dinheiro / cheque \n2 - À vista cartão \n3 - 2x no cartão \n4 - 3x ou mais no cartão: \n"))

if pagamento == 1:
    forma_pagamento = "à vista dinheiro / cheque, você terá 10% de desconto,"
    novo_preço = preço - (preço * 0.1)
    print(f'O preço normal do produto é R$ {preço:.2f}. Por você efetuar o pagamento {forma_pagamento} e irá pagar '
      f'R$ {novo_preço:.2f}.')
elif pagamento == 2:
    forma_pagamento = "à vista cartão, você terá 5% de desconto,"
    novo_preço = preço - (preço * 0.05)
    print(f'O preço normal do produto é R$ {preço:.2f}. Por você efetuar o pagamento {forma_pagamento} e irá pagar '
          f'R$ {novo_preço:.2f}.')
elif pagamento == 3:
    forma_pagamento = "em 2x no cartão, você não terá desconto,"
    novo_preço = preço
    print(f'O preço normal do produto é R$ {preço:.2f}. Por você efetuar o pagamento {forma_pagamento} e irá pagar '
          f'R$ {novo_preço:.2f}.')
elif pagamento == 4:
    parcelamento = int(input("Quantas parcelas? "))
    forma_pagamento = "você terá 20% de acréscimo sobre o preço normal do " \
                      "produto,"
    novo_preço = preço + (preço * 0.2)
    print(f'O preço normal do produto é R$ {preço:.2f}. Por você efetuar o pagamento em {parcelamento}'
          f' vezes no cartão, {forma_pagamento} e '
          f'irá '
          f'pagar '
          f'R$ {novo_preço:.2f}.')
else:
    forma_pagamento = 0
    print("Opção inválida de pagamento. Tente novamente.")
