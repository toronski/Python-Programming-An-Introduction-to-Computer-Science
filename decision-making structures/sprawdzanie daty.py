# sprawdzanie daty.py


def is_leap(year):
    leap = False 
    if year % 4 == 0:
        if year % 100 != 0 or year % 400 == 0:
            leap = True
    return leap

def main():
    is_valid = True
    date = input("Wpisz datę w formacie dd/mm/rrrr: ")
    days, month, year = date.split('/')
    days_31 = [1, 3, 5, 7, 8, 10, 12]

    try:
        month = int(month)
        days = int(days)
        year = int(year)

        if month > 12 or month < 1 or days > 31 or days < 1 or year < 1:
            is_valid = False
        elif month not in days_31 and day == 31:
            is_valid = False

        if is_leap(year) and month == 2 and days == 30:
            is_valid = False
        elif not is_leap(year) and month == 2 and day > 28:
            is_valid = False

    except:
        is_valid = False

        
    if is_valid:
        print("Data jest właściwa.")
    else: print("Data nie jest właściwa.")
    
main()
