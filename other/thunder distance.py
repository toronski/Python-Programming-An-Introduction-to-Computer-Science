# Program do obliczania odległości uderzenia piruna.

def main():
    print("Program do obliczania odległości uderzenia pioruna.")

    time = eval(input("Czas od błysku do grzmotu w sekundach: "))
    thunder_distance = time* 340.3
    thunder_dist_km = thunder_distance / 1000
    distance_rounded = round(thunder_dist_km, 3)

    print("Odległość od uderzenia pioruna wynosi: ", distance_rounded, "km.")

main()
