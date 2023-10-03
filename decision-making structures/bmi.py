# bmi.py

def main():
    waga = eval(input("Wpisz swoją wagę w kilogramach: "))
    wzrost = eval(input("Wpisz swój wzrost w metrach: "))
    bmi = waga / wzrost ** 2

    if bmi < 19:
        print("Twoje BMI jest za niskie({0:0.2f}).".format(bmi))
    elif bmi > 25:
        print("Twoje BMI jest za wysokie({0:0.2f}).".format(bmi))
    else:
        print("Twoje BMI jest dobre({0:0.2f}).".format(bmi))

main()
