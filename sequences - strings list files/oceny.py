# grade.py

def main():
    print("Program do ocen na podstawie punktacji")

    n = eval(input("Wpisz punktacje (od 0 do 5): "))

    oceny = ["F", "F", "D", "C", "B", "A"]

    print("Ocena ucznia to ", oceny[n])

main()
