'''import datetime
ano = int(input("Digite o ano para saber se é bissexto. Se quiser saber se o ano atual é bissexto, digite 0: "))
if ano == 0:
    ano = datetime.datetime.now().year
if str(ano)[-2:] == "00" and ano % 400 == 0:
    print(f"O ano {ano} é bissexto.")
elif str(ano)[-2:] == "00":
    print(f"O ano {ano} não é bissexto.")
elif ano % 4 == 0:
    print(f"O ano {ano} é bissexto.")
else:
    print(f"O ano {ano} não é bissexto.")'''

from datetime import date
ano = int(input("Que ano quer analisar? Coloque 0 para analisar o ano atual: "))
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print(f"O ano {ano} é BISSEXTO.")
else:
    print(f"O ano {ano} NÃO é BISSEXTO.")







