# maxval.py


def main():
    x1, x2, x3 = eval(input("Proszę wpisać 3 liczby: "))

    if x1 >= x2:
        if x1 >= x3:
            maxval = x1
        else:
            maxval = x3
    else:
        if x2 >= x3:
            maxval = x2
        else:
            maxval = x3

    print("Największa wartość to", maxval)

main()


maxval = x1
if x2 > maxval:
    maxval = x2
if x3 > maxval:
    maxval = x3
