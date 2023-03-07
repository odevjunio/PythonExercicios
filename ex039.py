'''from datetime import datetime, timedelta
sex = str(input("Informe seu sexo (F, para feminino / M, para masculino): "))

if sex == "M":
    birth = input("Data de nascimento no formato dd/mm/aaaa: ")
    birth_datetime = datetime.strptime(birth, '%d/%m/%Y')
    today = datetime.now()
    age_days = today - birth_datetime
    age_years = (age_days.total_seconds()) / 60 / 60 / 24 / 365.2425
    first_day_year = datetime(today.year, 1, 1)
    last_day_year = datetime(today.year, 12, 31)
    last_day_enlist = datetime(today.year, 6, 30)
    birthday_18 = birth_datetime.replace(year=birth_datetime.year + 18)
    birthday_17 = birth_datetime.replace(year=birth_datetime.year + 17)
    first_day_year_18 = datetime(birthday_18.year, 1, 1)
    last_day_enlist_18 = datetime(birthday_18.year, 6, 30)
    days_til_enlist = ((first_day_year_18 - today).total_seconds()) / 60 / 60 / 24
    days_after_enlist = ((today - last_day_enlist).total_seconds()) / 60 / 60 / 24
    days_after_enlist_18 = ((today - last_day_enlist_18).total_seconds()) / 60 / 60 / 24

    if age_years < 17.0:

        print(f"Você ainda tem {age_years:.0f} ano(s), mas entre os quatro primeiros meses do ano em que estiver "
              f"completando 18 anos você deverá se alistar.")
        print(f"Mas calma! Ainda faltam {days_til_enlist:.0f} dias para o início do período de alistamento, que ocorrerá "
              f"entre os dias {first_day_year_18.strftime('%d/%m/%Y')} e {last_day_enlist_18.strftime('%d/%m/%Y')}.")

    elif 17.0 <= age_years < 18.0 and first_day_year <= birthday_17 <= last_day_year:

        print(f"Você completa 17 anos em {birthday_17.strftime('%d/%m/%Y')}. Faltam {days_til_enlist:.0f} dias para o "
              f"início "
              f"do período de alistamento, "
              f"que ocorrerá entre os dias {first_day_year_18.strftime('%d/%m/%Y')} e {last_day_enlist_18.strftime('%d/%m/%Y')}.")

    elif 17.0 <= age_years < 19.0 and first_day_year <= birthday_18 <= last_day_year:

        if first_day_year <= today <= last_day_enlist:
            print(f"Esse ano você completa 18 anos em {birthday_18.strftime('%d/%m/%Y')}. Já está NA HORA DE SE ALISTAR! "
                  f"\nPeríodo de "
                  f"alistamento:"
                   f" {first_day_year.strftime('%d/%m/%Y')} a {last_day_enlist.strftime('%d/%m/%Y')}.")

        elif today > last_day_enlist:
            print(f"Esse ano você completa 18 anos e já se passaram {days_after_enlist:.0f} dias desde a data "
                  f"limite ({last_day_enlist.strftime('%d/%m/%Y')}) para você se alistar. Procure uma JUNTA DE SERVIÇO "
                  f"MILITAR!")

    elif age_years >= 19.0:
        print(f"Esse ano você completa {age_years:.0f} anos e já se passaram {days_after_enlist_18:.0f} dias "
              f"desde o final do período de alistamento do ano em que você completou 18 anos. \nPeríodo de alistamento: "
              f"{first_day_year_18.strftime('%d/%m/%Y')} a {last_day_enlist_18.strftime('%d/%m/%Y')}. \nProcure uma JUNTA DE SERVIÇO MILITAR!")

elif sex == "F":
    print("Apenas os jovens do SEXO MASCULINO que completarem 18 anos este ano devem se alistar para o Serviço "
          "Militar Obrigatório até 30 de junho.")
else:
    print("Digite F, para feminino ou M, para masculino!")
'''


from datetime import date
sex = str(input("Informe seu sexo (F, para feminino / M, para masculino): "))

if sex == "M":

    birth_year = int(input("Ano de nascimento (4 dígitos): "))
    this_year = date.today().year
    age = this_year - birth_year
    print(f"Quem nasceu em {birth_year} tem {age} anos em {this_year}.")
    years_til_alistam = 18 - age
    years_after_alistam = age - 18
    year_of_alistam = this_year - years_after_alistam

    if age < 18:
        print(f"Ainda falta(m) {years_til_alistam} ano(s) para o alistamento.")
        print(f"Seu alistamento será em {this_year + years_til_alistam}.")

    elif age == 18:
        print("Você tem que se alistar IMEDIATAMENTE!")

    else:
        print(f"Você já deveria ter se alistado há {years_after_alistam} ano(s).")
        print(f"Seu alistamento foi em {year_of_alistam}.")

elif sex == "F":
    print("Apenas os jovens do SEXO MASCULINO que completarem 18 anos este ano devem se alistar para o Serviço "
          "Militar Obrigatório até 30 de junho.")
else:
    print("Digite F, para feminino ou M, para masculino!")