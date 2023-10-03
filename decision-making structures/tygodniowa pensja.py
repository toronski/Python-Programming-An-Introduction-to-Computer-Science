# stawka godzinowa w tygodniu pracy.py

def main():
    n = eval(input("Wpisz liczbę godzin przepracowanych w tygodniu: "))
    hourly = eval(input("Wpisz stawkę za godzinę pracy: "))

    if n > 40:
        standardPay = 40 * hourly
        overtimePay = (n - 40) * (hourly * 1.5)
        pay = standardPay + overtimePay
        
    else:
        pay = n * hourly

    print("Twoja tygodniowa pensja wyniesie: ", pay)

main()
