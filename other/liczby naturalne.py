# Program do obliczania sumy odanych n liczb naturalnych.

def main():
    n = eval(input("Ilu liczb naturalnych chcesz otrzymać sumę: "))
    razem = 0

    for i in range(1, n + 1):
        razem = razem + i

    print("Suma ,", n, "liczb naturalnych wyniesie: ", razem)

main()


