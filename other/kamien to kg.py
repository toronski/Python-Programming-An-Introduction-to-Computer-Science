# Program konwersji masy w kamieniach na kilogramy

def main():
    print("Program konwersji masy ze staropolskich kamieni na kilogramy.")
    kamien = eval(input("Wpisz masę w kamieniach: "))
    kg = kamien * 12.96
    print(kamien, "kamieni to ", kg, " kilogramów.")

main()
