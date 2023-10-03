# mandat.py

def surplus(speed, limit):
    surplus = speed - limit
    return 5 * surplus

def main():
    limit = eval(input("Limit prędkości: "))
    speed = eval(input("zarejestrowana prędkość: "))

    if speed <= limit:
        print("Prędkość dopuszczona.")
    else:
        if speed > 90:
            ticket = 200 + 50 + surplus(speed, limit)
        else:
            ticket = 50 + surplus(speed, limit)

        print("Twój mandat wyniesie: ${0:0.2f}.".format(ticket))

main()
