def main():
    print("Ten program oblicza średnią punktów z trzech egzaminów.")

    score1, score2, score3 = eval(input("Wprowadź trzy oceny, oddzielone od siebie przecinkiem: "))
    average = (score1 + score2 + score3) / 3

    print("The average of the scores is:", average)

main()
