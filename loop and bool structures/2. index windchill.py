# index windchill

def main():
    print("\n" + " "*42 + "Windchill Factors")
    print("Wind" + " "*41 + "Temperature")
    print("Speed", end="")
    
    V = -20
    T = 0

    for T in range(-20, 61, 10):
        print(format(T, '10d'), end="")
    print()
    for V in range(0, 51, 5):
        print(format(V, '^5d'), end="")
        for T in range(-20, 61, 10):
            if V == 0:
                print(format(T, '10.1f'), end="")
            else:
                windchill = 35.74 + (0.6215*T) - 35.75*(V**0.16) + 0.4275*T*(V**0.16)
                print(format(windchill, '10.1f'), end="")
        print()
    print()
        

main()

