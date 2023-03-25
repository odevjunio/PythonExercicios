from datetime import date
print("======= Classificador de categoria da Confederação Nacional de Natação =======")
birth_year = int(input("Ano de nascimento (no formato aaaa): "))
today_year = date.today().year
age = today_year - birth_year

if age <= 9:
    categoria = "Até 9 anos: MIRIM."
elif age <= 14:
    categoria = "Até 14 anos: INFANTIL"
elif age <= 19:
    categoria = "Até 19 anos: JUNIOR"
elif age <= 25:
    categoria = "Até 25 anos: SÊNIOR"
else:
    categoria = "Acima de 25 anos: MASTER"

print(categoria)