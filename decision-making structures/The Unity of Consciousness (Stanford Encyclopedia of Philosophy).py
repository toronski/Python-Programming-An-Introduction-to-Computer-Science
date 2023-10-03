def is_leap(year):
    leap = False 
    if year % 4 == 0:
        if year % 100 != 0 or year % 400 == 0:
            leap = True
    return leap

def valid(day, month, year):
    is_valid = True
    days_31 = [1, 3, 5, 7, 8, 10, 12]

    try:
        if month > 12 or month < 1 or day > 31 or day < 1 or year < 1:
            is_valid = False
        elif month not in days_31 and day == 31:
            is_valid = False

        if is_leap(year) and month == 2 and day == 30:
            is_valid = False
        elif not is_leap(year) and month == 2 and day > 28:
            is_valid = False

    except:
        is_valid = False

        
    if is_valid:
        return True
    else: return False
    
def main():
    date = input("Wpisz datę w formacie dd/mm/rrrr: ")
    day, month, year = date.split('/')
    month = int(month)
    day = int(day)
    year = int(year)

    if valid(day, month, year):
        dayNum = 31 * (month - 1) + day

        if is_leap(year):
            if month > 2:
                dayNum += 1
        else:
            if month > 2:
                dayNum = dayNum - (((4 * month) + 23) // 10)

    else: print("Błąd daty.")

    print(dayNum, "dzień w roku wypada", date, ".")

main()
