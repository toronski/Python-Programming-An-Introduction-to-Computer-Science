# pensja opiekunki.py

def hours_convert(time_str):
    hours_str, minutes_str = time_str.split(":")
    hours = int(hours_str)
    minutes = int(minutes_str)
    return hours + minutes / 60

def main():
    pre_9_rate = 2.5
    post_9_rate = 1.75

    start_str = input("Wpisz godzinę rozpoczęcia pracy"\
                      "w formacie 24 godzinnym: ")
    start = hours_convert(start_str)
    end_str = input("Wpisz godzinę zakończenia pracy"\
                    "w formacie 24 godzinnym: ")
    end = hours_convert(end_str)

    if end < 21:
        cost = (end-start) * pre_9_rate
    elif start < 21 and end >= 21:
        cost = (21-start) * pre_9_rate + (end-21) * post_9_rate
    else:
        cost = (end-start) * post_9_rate

    print("Rachunek za opiekunkę wyniesie ${0:0.2f}.".format(cost))

main()
    
