# change2.py

def main():
    print("Change Counter\n")

    print("Podaj liczbę monet każdego rodzaju.")
    quarters = eval(input("Quarters: "))
    dimes = eval(input("Dimes: "))
    nickels = eval(input("Nickels: "))
    pennies = eval(input("Pennies: "))

    total =quarters * 25 + dimes * 10 + nickels * 5 + pennies

    print("Suma twoich monet wynosi ${0}.{1:0>2}"
          .format(total//100, total%100))

main()
