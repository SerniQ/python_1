# # post_code = input("podaj kod")
# # post_code = post_code.replace("-","")
# # letter_index = 0
# # good_code = ""
# #
# # while letter_index < len(post_code):
# #     if letter_index % 2 == 0 and letter_index != 0:
# #         good_code += "-"
# #     good_code += post_code[letter_index]
# #     letter_index += 1
# #
# # print(good_code)
#
# #
# # # Zamieniamy kod pocztowy by zawsze byĹ‚ zgodny z formatem XX-XX-XX-XX...
# # post_code = input("Jaki jest TwĂłj kod pocztowy? ")
# # post_code = post_code.replace("-", "")
# # formatted_post_code = ""
# # letter_index = 0
# # while letter_index < len(post_code):
# #     if letter_index % 2 == 0 and letter_index != 0:
# #         formatted_post_code += "-"
# #     formatted_post_code += post_code[letter_index]
# #     letter_index += 1
# # print(formatted_post_code)
# #
# # # Wypisujemy kod pocztowy - znak po znaku
# # post_code = input("Jaki jest TwĂłj kod pocztowy? ")
# # letter_index = 0
# # while letter_index < len(post_code):
# #     print(f"[{letter_index}] -> {post_code[letter_index]}")
# #     letter_index += 1
#
# # #
# # numer = input("jaki nr telefonu")
# # numer = numer.replace("-","")
# # numer = numer.replace(" ","")
# # good_nr = ""
# # letter_index = 0
# # while letter_index < len(numer):
# #     if letter_index % 3 == 0 and letter_index != 0:
# #         good_nr += "-"
# #     good_nr += numer[letter_index]
# #     letter_index += 1
# # print(good_nr)
# #
#
# # Zamieniamy kod pocztowy by zawsze byĹ‚ zgodny z formatem XX-XX-XX-XX...
# # phone_number = input("Podaj numer telefonu: ")
# # phone_number = phone_number.replace("-", "")
# # formatted_phone_number = ""
# # digit_index = 0
# # while digit_index < len(phone_number):
# #     if digit_index % 3 == 0 and digit_index != 0:
# #         formatted_phone_number += "-"
# #     formatted_phone_number += phone_number[digit_index]
# #     digit_index += 1
# #
# # print(f"TwÃ³j numer telefonu to: {formatted_phone_number}")
#
# # y = []
# # x = input("podaj dania po przecinku")
# # y = x.split(",")
# # index = 0
# # while index < len(y):
# #     print(index, "->", y[index])
# #     index += 1
#
# # exp = {
# #     "a": 123,
# #     "b": 1333
# # }
# #
# # for el in exp.items():
# #     print(el[0], el[1])
# #     print(type(el))
#
# # item = (1, 2)
# # name, value = item
# # print(name, value)
#
# # x = "12313"
# # counter = 0
# # for index, letter in enumerate(x):
# #     if index % 2 == 0 and index != 0:
# #         print(letter)
#
# # code = input("podaj kod")
# # code = code.replace(" ","").replace("-","")
# # good_code = ""
# # for index, letter in enumerate(code):
# #     if index % 2 == 0 and index != 0:
# #         good_code += "-"
# #     good_code += code[index]
# # print(good_code)
# # x = None
# # y =[]
# # while x != "X":
# #     if x != "X":
# #         x = input("podaj ocene")
# #         if x != "X":
# #             y += x
# # print(y)
# # suma = 0
# # for el in y:
# #     suma = suma + int(el)
# # print(y)
# # wynik = suma / len(y)
# # print("srednia:", wynik)
#
#
# wydatki = {}
# categ = input("Podaj kategorie wydatku lub jak nie to wpisz X")
# while categ != "X":
#     wydatki[categ] = []
#     wartosc = input("podaj wartosc lub X")
#     while wartosc != "X":
#         wydatki_value = float(wartosc)
#         wydatki[categ].append(wartosc)
#         wartosc = input("podaj wartosc lub X")
#     categ = input("Podaj kategorie wydatku lub jak nie to wpisz X")
#
# print(wydatki)
#
# total = 0
#
# # total_expenditures = 0
# # for category_expenditures in expenditures.values():
# #     for expenditure_value in category_expenditures:
# #         total_expenditures += expenditure_value
# #     # total_expenditures += sum(category_expenditures)
# #
# #
# # expenditures_percentage = {}
# # for category_name, category_expenditures in expenditures.items():
# #     total_category_expenditures = 0
# #     for expenditure_value in category_expenditures:
# #         total_category_expenditures += expenditure_value
# #     # total_category_expenditures = sum(category_expenditures)
# #     expenditures_percentage[category_name] = total_category_expenditures * 100 / total_expenditures
# #
# # most_important_category = None
# # most_important_category_percentage = 0
# # for category, percentage in expenditures_percentage.items():
# #     if percentage > most_important_category_percentage:
# #         most_important_category_percentage = percentage
# #         most_important_category = category
# #
# # if most_important_category is not None:
# #     print(f"Najwięcej wydajesz na {most_important_category} - {most_important_category_percentage:.0f}% wszystkich wydatków")
# #
# # for category, percentage in expenditures_percentage.items():
# #     print(f"Na {category} wydajesz {percentage:.0f}% miesięcznych wydatków")
#

# x = input("Podaj nr")
# for digit in range(20):
#     digit_times = x.count(str(digit))
#     print(digit, digit_times)

    # Napisz kalkulator dla kredytu o malejącej racie. Zapytaj użytkownika o:

# Napisz kalkulator dla kredytu o malejącej racie. Zapytaj użytkownika o:
# -> Kwotę kredytu
# -> Oprocentowanie kredytu
# -> Czas trwania (w latach)
# -> Koszty początkowe (prowizja itp.)
# Oblicz jaką łącznie sumę użytkownik odda bankowi i porównaj ją z kapitałem, który otrzyma.
# Podpowiedź: oblicz wartość każdej miesięcznej raty według wzoru:
# kapitał spłacany miesięcznie = kwota kredytu / (liczba lat * 12)
# pozostały kapitał = kwota kredytu - (numer miesiąca od początku - 1) * kapitał spłacany miesięcznie
# rata = (pozostały kapitał * oprocentowanie / 100) / 12 + kapitał spłacany miesięcznie

capital = int(input("Na jaką kwotę jest kredyt? "))
interest_rate = float(input("Jakie jest oprocentowanie (%)? "))
years = int(input("Na ile lat jest kredyt? "))
initial_fees = int(input("Jakie są koszty początkowe? "))

credit_time_in_months = years * 12
monthly_paid_capital = capital / credit_time_in_months
total_paid = initial_fees
for month_number in range(1, credit_time_in_months + 1):
    capital_to_be_paid = capital - (month_number - 1) * monthly_paid_capital
    installment = (capital_to_be_paid * interest_rate / 100) / 12 + monthly_paid_capital
    total_paid += installment
    print(f"Rata w miesiącu {month_number} wyniesie {installment:.2f}")

print(f"Zaciągając {capital} na tych warunkach spłacisz z odsetkami {total_paid}")

distance = 38
time = 3
speed = distane / time
print(speed)
Print
print(22)

